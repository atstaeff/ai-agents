---
marp: true
theme: default
paginate: true
header: "Project Review"
footer: "Sprint {N} — © 2026"
style: |
  section {
    font-family: 'Inter', 'Segoe UI', sans-serif;
    background-color: #f7fafc;
    color: #2d3748;
  }
  h1 {
    color: #2b6cb0;
    border-bottom: 2px solid #2b6cb0;
    padding-bottom: 0.2em;
  }
  h2 {
    color: #4a5568;
  }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }
  .status-green { color: #38a169; font-weight: bold; }
  .status-yellow { color: #d69e2e; font-weight: bold; }
  .status-red { color: #e53e3e; font-weight: bold; }
  blockquote {
    border-left: 4px solid #2b6cb0;
    padding-left: 1em;
    color: #718096;
  }
  table {
    font-size: 0.85em;
  }
---

<!-- _class: lead -->

# Project Review
## {Project Name} — Sprint {N}

**Date:** {Date}
**Status:** <span class="status-green">🟢 On Track</span>

---

# Executive Summary

- ✅ **Sprint Goal achieved:** {What we delivered}
- 📊 **Velocity:** {X} story points completed
- 🎯 **Quality:** {X}% test coverage, 0 critical bugs
- 📅 **On track** for {milestone} delivery by {date}

> Key highlight: {One-sentence achievement that stakeholders care about}

---

# Sprint Achievements

| # | Deliverable | Status | Impact |
|---|------------|--------|--------|
| 1 | {Feature/task 1} | ✅ Done | {Business impact} |
| 2 | {Feature/task 2} | ✅ Done | {Business impact} |
| 3 | {Feature/task 3} | ✅ Done | {Business impact} |
| 4 | {Feature/task 4} | 🔵 90% | {Expected by tomorrow} |

---

# Milestone Progress

| Milestone | Target | Status | Progress |
|-----------|--------|--------|----------|
| MVP Core Features | Week 6 | 🟢 | ████████░░ 80% |
| API Integration | Week 8 | 🟡 | █████░░░░░ 50% |
| Security Hardening | Week 10 | 🟢 | ███░░░░░░░ 30% |
| Go-Live | Week 12 | 🟢 | ██░░░░░░░░ 20% |

---

# Quality Metrics

<div class="columns">

**Code Quality**
- Test Coverage: **82%** ✅
- Type Coverage: **95%** ✅
- Lint Warnings: **0** ✅
- Security Issues: **0** ✅

**Operational Health**
- Uptime (Staging): **99.8%**
- P99 Latency: **145ms**
- Error Rate: **0.02%**
- Deploy Frequency: **3x/week**

</div>

---

# Velocity & Burndown

| Sprint | Committed | Completed | Velocity |
|--------|-----------|-----------|----------|
| Sprint 1 | 21 SP | 18 SP | 18 |
| Sprint 2 | 21 SP | 21 SP | 21 |
| Sprint 3 | 24 SP | 22 SP | 22 |
| **Sprint {N}** | **{X} SP** | **{X} SP** | **{X}** |

**Average Velocity:** {X} SP/sprint
**Projected Completion:** On schedule

---

# Risks & Mitigations

| Risk | Likelihood | Impact | Status | Mitigation |
|------|-----------|--------|--------|------------|
| {Risk 1} | Medium | High | 🟡 Active | {What we're doing} |
| {Risk 2} | Low | Medium | 🟢 Monitored | {Prevention strategy} |
| {Risk 3} | Low | Low | 🟢 Accepted | {Contingency plan} |

---

# Blockers & Dependencies

### Current Blockers
- 🔴 {Blocker 1} — **Owner:** {name}, **ETA:** {date}

### Dependencies
- ⏳ {Dependency 1} — Waiting on {team/person}
- ✅ {Dependency 2} — Resolved

### Decisions Needed
- 📋 {Decision 1} — By {person}, by {date}

---

# Budget Status

| Category | Budget | Spent | Remaining |
|----------|--------|-------|-----------|
| Development | €{XX,XXX} | €{XX,XXX} | €{X,XXX} |
| Infrastructure | €{X,XXX} | €{X,XXX} | €{XXX} |
| **Total** | **€{XX,XXX}** | **€{XX,XXX}** | **€{X,XXX}** |

**Forecast:** ✅ On Budget

---

# Next Sprint Plan

### Sprint Goal
> {What we aim to achieve next sprint}

| # | Task | Priority | Estimate |
|---|------|----------|----------|
| 1 | {Task 1} | P0 | {X} SP |
| 2 | {Task 2} | P0 | {X} SP |
| 3 | {Task 3} | P1 | {X} SP |
| 4 | {Task 4} | P1 | {X} SP |

**Planned Velocity:** {X} SP

---

# Roadmap Outlook

| Phase | Timeline | Focus |
|-------|----------|-------|
| **Now** (Sprint {N}) | {Dates} | {Current focus} |
| **Next** (Sprint {N+1}) | {Dates} | {Upcoming focus} |
| **Later** (Sprint {N+2-3}) | {Dates} | {Future focus} |
| **Launch** | {Date} | Go-live preparation |

---

# Key Takeaways

1. ✅ {Main achievement} — impact on timeline/quality
2. 📊 {Metric improvement} — quantified result
3. 🎯 {Strategic alignment} — progress toward business goal
4. ⚠️ {Attention item} — what needs monitoring

---

<!-- _class: lead -->

# Questions & Discussion

**Next Review:** {Date}
**Sprint {N+1} Start:** {Date}
