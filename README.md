# Interaction Design CA1: Presentation Specification & Instruction Document
## Project Topic: UX Analysis of College Golf Cart App

> **IMPORTANT SPECIFICATION NOTICE FOR AI / DEVELOPER:**  
> This document serves as the **master specification and instruction manual** for generating the Interaction Design CA1 presentation deck.  
> **CRITICAL RULE:** This project is strictly focused on **PROBLEM IDENTIFICATION and USER RESEARCH**. It is **NOT** a solution or redesign project. Do not include mockups, wireframes, or proposed feature UI solutions in the final presentation.

---

## 1. Project Overview & Scope

### Project Summary
The goal of this CA1 assignment is to evaluate the existing mobile application used by students to access campus golf cart transportation services, identify critical user experience friction points through primary and secondary user research, and formulate an evidence-backed human-centered Problem Statement and "How Might We" (HMW) question.

### Core Problem Selected
> **"Uncertainty about golf cart arrival time, real-time location and seat availability."**

---

## 2. Core Data & Evidence Inventory

The following empirical research data must be presented with 100% fidelity. **DO NOT modify, extrapolate, or fabricate any numerical statistics or qualitative responses.**

### A. Quantitative Survey Data (Google Forms)
* **Sample Size Context:** Most questions have $N=19$ respondents; overall usability has $N=20$ respondents.

| Question / Metric | Empirical Data & Distribution | Key Analytical Takeaway |
| :--- | :--- | :--- |
| **Q1: Arrival Difficulty**<br>`"Have you experienced difficulty in determining when the next golf cart will arrive?"` | • **YES:** 78.9% (15 out of 19)<br>• **NO:** 21.1% (4 out of 19) | **78.9%** of users experience friction tracking cart arrival. |
| **Q2: Seat Availability Clarity**<br>`"How clearly does the app display the availability of seats in the golf cart?"` | • **Not Clearly:** 52.6% (10/19)<br>• **Not Noticed:** 36.8% (7/19)<br>• **Clearly:** 10.5% (2/19) | **89.4%** find seat availability unclear or unnoticeable. |
| **Q3: Impact on Rides**<br>`"Have you ever missed a golf cart or waited longer than expected due to a lack of accurate arrival information?"` | • **Yes, frequently:** 52.6% (10/19)<br>• **Yes, occasionally:** 36.8% (7/19)<br>• **No:** 10.5% (2/19) | **89.4%** have missed rides or experienced unexpected long waits. |
| **Q4: Fare Calculation Transparency**<br>`"How well do you understand the calculation of the ₹15 golf cart fare?"` | • **Not understand:** 52.6% (10/19)<br>• **Not aware:** 26.3% (5/19)<br>• **Understand:** 21.1% (4/19) | **78.9%** lack clear understanding of fare calculation. |
| **Q5: Overall App Usability**<br>`"How would you rate the overall usability of the College Golf Cart App?"` | • **Rating 1:** 30% (6/20)<br>• **Rating 2:** 20% (4/20)<br>• **Rating 3:** 20% (4/20)<br>• **Rating 4:** 30% (6/20)<br>• **Rating 5:** 0% (0/20) | **50%** rated usability low ($\le 2$), with 0% giving a 5/5 score. *(Present exact distribution, do not compute average).* |

### B. Qualitative Survey Themes (Open-Ended Responses)
Synthesize the open-ended user feedback under these exact qualitative themes:
* **Real-time Location:** Cart location fails to update in real-time or is completely absent.
* **Arrival Predictability:** High uncertainty regarding waiting duration and inaccurate ETAs.
* **Seat Availability:** Complete lack of live seat occupancy indicators before cart arrival.
* **Peak Time Bottlenecks:** Severe shortage of golf carts during morning peak hours (hostel to academic blocks).
* **Directional Clarity:** Need to identify cart trajectory (e.g., heading toward hostel vs. academic block).
* **Navigation & Transparency:** Desire for clearer route info, upfront fare calculation breakdowns, push notifications when carts approach, and a simplified interface for reporting issues.

---

## 3. Initial Problem Exploration vs. Selected Problem

### Initial Problem Exploration (3–5 Candidate UX Issues)
Before focusing on the primary issue, the research identified 5 initial UX friction points:
1. **Unclear real-time golf cart location**
2. **Unclear/inaccurate arrival time**
3. **Lack of clear seat availability information**
4. **Limited route and ride information**
5. **Confusing fare calculation structure**

### Research Synthesis & Problem Selection
Rather than treating these as isolated UI bugs, research demonstrates they stem from an overarching root issue:
> **"Uncertainty while waiting for and planning a golf cart ride."**

#### User Journey: The Friction Cycle
```
[Student needs a golf cart on campus]
                  │
                  ▼
          [Opens Golf Cart App]
                  │
                  ▼
   [Wants arrival time, location, & seat info]
                  │
                  ▼
   [Information missing or inaccurate]
                  │
                  ▼
       [Waits / Checks app repeatedly]
                  │
                  ▼
[Misses cart or experiences long unexpected wait]
```

---

## 4. Synthesis & Artifact Frameworks

### A. Target User Profile
* **Primary Demographic:** College students relying on campus golf carts for daily intra-campus transit.
* **Primary Context:** Traveling between hostels, academic blocks, dining halls, and campus gates.
* **User Mindset:** Time-sensitive travel, planning movement between classes, avoiding tardiness.

### B. Empathy Map Synthesis

| Quadrant | Content (Research-Informed Synthesis) |
| :--- | :--- |
| **SAYS** | • *"When will the cart actually arrive?"*<br>• *"Is there an empty seat for me?"*<br>• *"Where is the golf cart right now?"* |
| **THINKS** | • *"Should I keep standing here or start walking?"*<br>• *"Is the location on the screen accurate?"*<br>• *"Am I going to be late for my class?"* |
| **DOES** | • Repeatedly refreshes and checks the app interface.<br>• Waits at designated pickup points looking down the road.<br>• Attempts to flag down carts without knowing seat availability. |
| **FEELS** | • **Confused** by unclear arrival data.<br>• **Uncertain** about ride reliability.<br>• **Frustrated** by missed carts and unexpected delays.<br>• **Anxious** about campus class schedules. |

### C. Synthesized User Needs & Pain Points

```
┌──────────────────────────────────────────────┬──────────────────────────────────────────────┐
│                  PAIN POINTS                 │                  USER NEEDS                  │
├──────────────────────────────────────────────┼──────────────────────────────────────────────┤
│ • High uncertainty while waiting at stops    │ • Clear, real-time cart location tracking    │
│ • Inaccurate or missing ETA information      │ • Accurate & reliable Estimated Arrival Time │
│ • Inability to check seat occupancy upfront │ • Visible live seat availability indicators   │
│ • Repeatedly reopening/checking the app      │ • Timely proximity notifications             │
│ • Risk of missing carts & schedule delays    │ • Clear route & direction information        │
│ • Ambiguity in fare calculation              │ • Transparent fare breakdown & easy support  │
└──────────────────────────────────────────────┴──────────────────────────────────────────────┘
```

---

## 5. Master Presentation Slide Structure (14-Slide Blueprint)

The presentation deck must be generated following this exact slide hierarchy and layout guide:

### SLIDE 1: Title Slide
* **Title:** Improving the College Golf Cart App Experience
* **Subtitle:** Interaction Design CA1 — UX Problem Identification & User Research
* **Visual Elements:** High-contrast header card, subtle campus transit badge, clean minimalist layout.

### SLIDE 2: About the Existing App
* **Content:** Overview of the current college golf cart service and mobile app interface.
* **Assets:** App screenshots (`Home`, `Wallet`, `Profile`, `Rides`).
* **Visual Layout:** 4-column screenshot card grid with descriptive annotations highlighting current interface modules.

### SLIDE 3: Initial Problem Exploration
* **Content:** Introduction of 3–5 initial UX friction points discovered during initial audit.
* **Items:** Location clarity, ETA accuracy, seat communication, route info, fare structure.
* **Visual Layout:** 5 balanced feature-card containers leading toward an exploratory overview note.

### SLIDE 4: Selected Problem & User Journey
* **Content:** Focus on the core problem: *"Uncertainty about golf cart arrival time, real-time location and seat availability."*
* **Visual Layout:** Top callout card highlighting the selected problem + a vertical/horizontal step-by-step User Journey diagram illustrating student friction from app opening to missed cart.

### SLIDE 5: Research Methodology
* **Content:** Overview of research triangulation approach:
  1. **Google Form Survey:** 19–20 student responses.
  2. **User Interviews:** 5 contextual student interviews.
  3. **User Observation:** Campus transit stop observation.
  4. **Secondary Research:** 3+ industry articles & mobility papers.
* **Visual Layout:** 4-quadrant methodology grid with icons and sample counts.

### SLIDE 6: Primary Research — Arrival & Waiting (Google Form)
* **Content:** Statistical breakdown of Q1 & Q3.
* **Key Metrics:**
  * **78.9%** (15/19) difficulty determining cart arrival.
  * **89.4%** (17/19) experienced missed carts or unexpected long waits.
* **Assets:** Pie/Bar charts from Google Form screenshots.
* **Visual Layout:** 2 side-by-side metric hero cards with big percentage typography and supporting charts.

### SLIDE 7: Primary Research — Seats & Fare Understanding (Google Form)
* **Content:** Statistical breakdown of Q2 & Q4.
* **Key Metrics:**
  * **89.4%** report seat availability is unclear (52.6%) or unnoticed (36.8%).
  * **78.9%** do not understand (52.6%) or are unaware of (26.3%) the ₹15 fare calculation.
* **Assets:** Survey result charts.
* **Visual Layout:** Dual-card layout featuring exact chart crops and high-impact stat callouts.

### SLIDE 8: Qualitative Research — Student Voice & Themes
* **Content:** Real open-ended feedback themes from survey respondents.
* **Themes:** Live tracking demand, ETA reliability, seat occupancy visibility, peak morning rush, directional indicators.
* **Assets:** Screenshots of written survey feedback.
* **Visual Layout:** Clean quote card layout displaying actual verbatim feedback snippets grouped by research theme.

### SLIDE 9: Primary Research — User Interviews & Observation
* **Content:** Summary of contextual interviews and observation.
* **Assets:** 5 User Interview photo/screenshot cards.
* **Placeholder:** `[Observation findings to be added from actual campus observation]`
* **Visual Layout:** 5 interview photo thumbnails paired with short factual observation bullets.

### SLIDE 10: Secondary Research & Industry Context
* **Content:** Insights from secondary sources (articles, urban micro-mobility reports, transit UX studies).
* **Assets:** 3 article/source screenshots.
* **Structure per source:** Source Title, Image, Key Finding, Relevance to Campus Golf Cart UX.
* **Visual Layout:** 3 horizontal card rows clearly labeled as SECONDARY RESEARCH.

### SLIDE 11: Empathy Mapping
* **Content:** 4-quadrant Empathy Map (Says, Thinks, Does, Feels).
* **Visual Layout:** 2x2 grid with distinct accent colors for each quadrant, using research-informed student bullet points.

### SLIDE 12: Research Analysis — Pain Points & User Needs
* **Content:** Comprehensive synthesis of user friction vs. core requirements.
* **Visual Layout:** Two-column comparative matrix (Pain Points on left in subtle rose/gray cards, User Needs on right in slate/blue cards).

### SLIDE 13: Final Problem Statement
* **Content:** Human-centered problem statement:
  > *"College students need a clear and reliable way to know the real-time location, arrival time and seat availability of golf carts because the current app does not communicate this information clearly, causing uncertainty, longer waiting times and missed rides."*
* **Visual Layout:** Premium full-width banner card with large, highly legible typography and key concept highlights.

### SLIDE 14: How Might We? (HMW) & References
* **Content:**
  * **HMW Question:** *"How might we help college students easily know when a golf cart will arrive and whether seats are available?"*
  * **References:** Citation list of secondary research articles and primary data sources.
* **Visual Layout:** Split slide with a bold HMW hero callout box on top and structured reference link items on the bottom.

---

## 6. Visual Design System & Aesthetic Guidelines

To achieve a **world-class modern UI/UX Case Study aesthetic**, enforce the following styling rules:

### Color Palette
* **Primary Accent:** Slate Blue (`#2563EB` / `#1D4ED8`) - inspired by the app theme.
* **Background:** Clean White (`#FFFFFF`) or Ultra-light Gray (`#F8FAFC`).
* **Card Containers:** Pure White (`#FFFFFF`) with subtle border (`#E2E8F0`) and soft shadow (`0 4px 6px -1px rgba(0,0,0,0.05)`).
* **Text Primary:** Deep Slate (`#0F172A`).
* **Text Secondary:** Slate Gray (`#475569`).
* **Highlight / Alert:** Soft Amber (`#F59E0B`) or Soft Red (`#EF4444`) for friction callouts.

### Typography & Structure
* **Font Family:** Clean sans-serif (Inter, Roboto, or Outfit).
* **Stat Callouts:** Extra Large Bold Typography (e.g., `78.9%`, `89.4%`) with label subtext.
* **Hierarchy:** Clear distinction between Slide Headers (28-32pt Bold), Card Titles (16-18pt Semi-bold), and Body/Bullets (12-14pt Regular).

### Content & Layout Rules
* **Whitespace:** Ensure generous padding around cards and text blocks. Never crowd slides.
* **Data Visualization:** Present percentages inside rounded stat cards adjacent to original chart assets.
* **No Solution UI:** Do NOT include wireframes, redesign concepts, or new UI buttons. Keep content strictly focused on problem analysis.

---

## 7. Data Integrity & Content Rules

1. **Zero Fabrication:** Never invent survey percentages, interview quotes, observation data, or article titles.
2. **Preserve Survey Language:** Keep exact wording of original survey questions intact.
3. **No Fake Averages:** Do not calculate an "average rating" for Q5 usability; display the exact 1-to-5 distribution.
4. **Clear Attribution:** Always maintain clear separation between **PRIMARY RESEARCH** (Forms, Interviews, Observation) and **SECONDARY RESEARCH** (Articles/Papers).
5. **Placeholders:** When data is pending (e.g., observation details), use explicit placeholders (`[Observation data to be added]`).

---

## 8. Asset Mapping Specification

When building the final presentation deck, reference assets from the following standardized directory structure:

```
/assets/
├── app-screenshots/
│   ├── home_screen.png          # App Home screen screenshot
│   ├── wallet_screen.png        # App Wallet screen screenshot
│   ├── profile_screen.png       # App Profile screen screenshot
│   └── rides_screen.png         # App Rides screen screenshot
│
├── google-form/
│   ├── chart_q1_arrival.png     # Q1 arrival difficulty chart
│   ├── chart_q2_seats.png       # Q2 seat availability chart
│   ├── chart_q3_waited.png      # Q3 missed cart / wait chart
│   ├── chart_q4_fare.png        # Q4 fare understanding chart
│   ├── chart_q5_usability.png   # Q5 usability rating chart
│   └── feedback_responses_*.png # 7-8 written feedback screenshots
│
├── user-interviews/
│   ├── interview_1.png          # Interview evidence 1
│   ├── interview_2.png          # Interview evidence 2
│   ├── interview_3.png          # Interview evidence 3
│   ├── interview_4.png          # Interview evidence 4
│   └── interview_5.png          # Interview evidence 5
│
└── secondary-research/
    ├── source_1_article.png     # Secondary article/paper screenshot 1
    ├── source_2_article.png     # Secondary article/paper screenshot 2
    └── source_3_article.png     # Secondary article/paper screenshot 3
```

---
*End of README.md Specification Document.*
