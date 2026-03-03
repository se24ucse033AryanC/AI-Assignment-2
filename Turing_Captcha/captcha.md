# CAPTCHA Implementation

## Objective
CAPTCHA distinguishes between humans and automated bots.

---

## Architecture

Components:
1. Random Text Generator
2. Image Generator
3. Distortion Module
4. Verification Module

---

## Working Process

1. System generates random string.
2. String is distorted visually.
3. User enters displayed text.
4. System compares input with stored value.
5. If match → Human verified.

---

## Agent Perspective

CAPTCHA system:
- Acts as validation agent.
- Uses pattern recognition resistance.
- Prevents automated bots.