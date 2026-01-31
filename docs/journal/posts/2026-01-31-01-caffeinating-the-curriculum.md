---
date: 2026-01-31 10:39:33
authors:
  - rob
categories:
  - Golang
  - React
  - Raspberry Pi
  - Digital Signage
  - Case Study
---

# Caffeinating the Curriculum: Building a Resilient Digital Menu Kiosk

**The Mission:** Upgrade a high school coffee shop's menu from paper and tape to a dynamic, commercial-grade digital display.

My latest project wasn't for a corporate client or a security audit; it was for the **Roaring Roasting Grounds**, a student-run coffee shop operated by the FCCLA (Family, Career and Community Leaders of America) and Culinary Arts department at the local high school.

They had a classic problem: a static menu that couldn't keep up with reality. Prices changed, "Dirty Sodas" were added, and syrups ran out mid-shift. They needed a digital signage solution that looked professional, was easy for students to update, and—most importantly—cost almost nothing.

## The Constraints

As a Security Compliance Manager, I’m used to working within strict boundaries. This environment was no different, but the constraints were physical rather than regulatory:

1.  **Air-Gapped (Effectively):** The device cannot rely on school WiFi. It must be fully offline-capable.
2.  **No Peripherals:** The final install is a TV mounted on a wall. No keyboard, no mouse attached during operation.
3.  **Non-Technical Operators:** The interface had to be "student-proof."
4.  **Resilience:** It needed to survive the "pull the plug" shutdown method every single day.

## The Architecture

I decided to over-engineer this slightly to ensure stability. Instead of a simple slideshow, I built a full-stack web application hosted locally on the device.

* **Hardware:** Raspberry Pi (running Pi OS Lite / Headless).
* **Backend:** **Go (Golang)**. I chose Go for its ability to compile down to a single, lightweight binary that manages the SQLite database and serves the API.
* **Frontend:** **React**. A dynamic SPA (Single Page Application) that polls the server every 15 seconds for changes.
* **Display:** Chromium running in Kiosk mode on top of a lightweight X11 window manager (Openbox).

## Feature Spotlight: "The 86 Board"

The coolest part of the build is the **Admin Panel**. I hid a secret button in the footer of the menu (the *Baking & Pastry* logo). When double-tapped, it prompts for a password.

Once inside, the students can:

* **"86" Items:** Instantly hide items that are out of stock.
* **Limit Items:** Mark specials as "Limited Quantity" (adds an orange badge).
* **Price Check:** Update prices on the fly.
* **Audit Logs:** A logging system allows the teacher to see exactly who changed what and when.

## Root Cause Analysis: Technical Challenges

### Challenge 1: The Time Travel Paradox

The biggest technical hurdle was time. Raspberry Pis do not have an internal Real-Time Clock (RTC) battery. Since the device is offline, every time they unplugged it, the Pi woke up thinking it was the year 1970 (or the last saved timestamp).

This completely broke my Audit Logs.

**The Fix:** I built a manual "Time Sync" into the Admin Panel. Since the students verify the menu every morning, they can hit `🕒 SET CLOCK`, input the current time from their phone, and the Go backend force-updates the system time via the Linux command line. It’s a low-tech solution to a high-tech problem.

### Challenge 2: The "Zombie Kiosk" Boot

Getting the Pi to boot reliably without a desktop environment was the final boss. I used `systemd` to orchestrate the startup.

The backend service launches first. Once the API is live, the Kiosk service triggers `startx`. We ran into race conditions where the video drivers weren't ready before the browser launched, leading to a permanent black screen on boot.

!!! failure "The Crash"
    When the Pi booted cold, `startx` would attempt to launch before the TTY or video drivers were initialized. The service would fail instantly and mark itself as "dead."

!!! success "The Fix"
    I hardened the systemd service with a `RestartSec=5` delay and strict TTY allocation. Now, the system handles "cold boots" perfectly: it fails gracefully, waits 5 seconds for the drivers to settle, and relaunches the UI automatically.

Here is the final systemd configuration that saved the day:

```ini title="/etc/systemd/system/menu-kiosk.service"
[Unit]
Description=Menu Kiosk Browser
After=network.target menu-server.service systemd-user-sessions.service

[Service]
User=rob
Group=rob
Environment=DISPLAY=:0
# Give it a dedicated terminal so startx doesn't get confused
TTYPath=/dev/tty7
StandardInput=tty

# The command to start the GUI
ExecStart=/usr/bin/startx

# CRITICAL: If it fails (because video wasn't ready), wait 5s and try again
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target