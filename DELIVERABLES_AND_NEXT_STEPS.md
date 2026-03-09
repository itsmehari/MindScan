# MindScan – Deliverables & What You Still Need To Do

## Deliverables Completed

| Item | Location |
|------|----------|
| **Consolidated project report (Markdown)** | `mindscan_project_report.md` (with college front matter and placeholders) |
| **Presentation (Marp-ready Markdown)** | `MindScan_Presentation.md` (use `---` slide breaks; add `marp: true` in front matter for Marp) |
| **Report as DOCX** | `MindScan_Project_Report.docx` (generated via Pandoc) |

---

## What You Still Need To Do

1. **Fill placeholders** in the report and presentation:
   - `[College Name (Full)]`, `[College Address – City, PIN]`
   - `[Your Full Name]`, `[Your Roll No]`
   - `[Guide Name]`, `[Guide Designation]`, `[HOD Name]`, `[Principal Name]`
   - `[Academic Year]` (e.g. 2024 – 2025)
   - `[Date]` and `[City]` where needed  
   If you don’t know the college address, search: *“[College name] [location] address”* and use the official details.

2. **In Word (DOCX):**
   - Add a **Table of Contents** (References → Table of Contents).
   - Insert **screenshots** of the app (journal page, dashboard) in the Implementation/Results sections if required.
   - Replace placeholder lines with actual **signatures** (or leave as-is for print-and-sign).

3. **Export presentation to PPTX:**
   - **If you use Marp:** Open `MindScan_Presentation.md` in Marp (VS Code Marp extension or Marp CLI) and export to PPTX.
   - **If you use Pandoc:**  
     `pandoc MindScan_Presentation.md -o MindScan_Presentation.pptx`  
     (Slide breaks are already `---`; you may need to adjust theme/size in the DOCX or use a reference doc.)

4. **Optional:** Rename `mindscan_project_report.md` to `MindScan_Project_Report.md` for submission naming (content is the same).

---

## Quick Pandoc Commands (for reference)

**Report MD → DOCX:**
```bash
pandoc mindscan_project_report.md -o MindScan_Project_Report.docx
```

**Presentation MD → PPTX (basic):**
```bash
pandoc MindScan_Presentation.md -o MindScan_Presentation.pptx
```

Run these from the project root: `E:\OneDrive\Glor\Others-Project\MindScan`
