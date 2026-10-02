import sys
import re
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.lib import colors


BASE_DIR = Path(__file__).resolve().parent.parent

ANALYSIS_DIR = BASE_DIR / "analysis"
REPORTS_DIR = BASE_DIR / "reports"


def markdown_to_reportlab(text):
    # Escape characters that ReportLab Paragraph treats as XML/HTML.
    text = (
        text
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )

    # Basic Markdown formatting.
    text = re.sub(
        r"`([^`]+)`",
        r"<font name='Courier'>\1</font>",
        text
    )

    text = re.sub(
        r"\*\*(.+?)\*\*",
        r"<b>\1</b>",
        text
    )

    text = re.sub(
        r"(?<!\*)\*([^*]+)\*(?!\*)",
        r"<i>\1</i>",
        text
    )

    # Markdown links -> visible link text only.
    text = re.sub(
        r"\[([^\]]+)\]\([^)]+\)",
        r"\1",
        text
    )

    return text


def create_styles():
    styles = getSampleStyleSheet()

    title = styles["Title"]
    title.alignment = TA_CENTER

    heading1 = ParagraphStyle(
        "ReportHeading1",
        parent=styles["Heading1"],
        spaceBefore=14,
        spaceAfter=8,
    )

    heading2 = ParagraphStyle(
        "ReportHeading2",
        parent=styles["Heading2"],
        spaceBefore=12,
        spaceAfter=6,
    )

    heading3 = ParagraphStyle(
        "ReportHeading3",
        parent=styles["Heading3"],
        spaceBefore=8,
        spaceAfter=4,
    )

    body = ParagraphStyle(
        "ReportBody",
        parent=styles["BodyText"],
        leading=14,
        spaceAfter=7,
    )

    bullet = ParagraphStyle(
        "ReportBullet",
        parent=body,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=4,
    )

    table_text = ParagraphStyle(
        "ReportTableText",
        parent=styles["BodyText"],
        fontSize=8.5,
        leading=11,
    )

    return {
        "title": title,
        "heading1": heading1,
        "heading2": heading2,
        "heading3": heading3,
        "table": table_text,
        "body": body,
        "bullet": bullet,
    }


def split_table_row(line):
    line = line.strip()

    if line.startswith("|"):
        line = line[1:]

    if line.endswith("|"):
        line = line[:-1]

    return [cell.strip() for cell in line.split("|")]


def is_table_separator(line):
    cells = split_table_row(line)

    if not cells:
        return False

    return all(
        re.fullmatch(r":?-+:?", cell.strip())
        for cell in cells
    )


def build_table(lines, styles):
    rows = []

    for line in lines:
        if is_table_separator(line):
            continue

        cells = split_table_row(line)

        converted_cells = [
            Paragraph(
                markdown_to_reportlab(cell),
                styles["table"]
            )
            for cell in cells
        ]

        rows.append(converted_cells)

    if not rows:
        return None

    column_count = max(len(row) for row in rows)

    for row in rows:
        while len(row) < column_count:
            row.append(
                Paragraph("", styles["table"])
            )

    available_width = 470
    column_width = available_width / column_count

    table = Table(
        rows,
        colWidths=[column_width] * column_count,
        repeatRows=1,
    )

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))

    return table


def build_report(case_id):
    analysis_path = ANALYSIS_DIR / f"{case_id}.md"
    output_path = REPORTS_DIR / f"{case_id}-report.pdf"

    if not analysis_path.exists():
        print(f"Error: {analysis_path} not found.")
        return False

    REPORTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        analysis_path,
        "r",
        encoding="utf-8"
    ) as f:
        lines = f.read().splitlines()

    styles = create_styles()

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=45,
        leftMargin=45,
        topMargin=45,
        bottomMargin=45,
    )

    story = []

    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if not line:
            i += 1
            continue

        # Markdown table.
        if (
            "|" in line
            and i + 1 < len(lines)
            and "|" in lines[i + 1]
            and is_table_separator(lines[i + 1])
        ):
            table_lines = [line]
            i += 1

            while i < len(lines):
                current = lines[i].strip()

                if not current or "|" not in current:
                    break

                table_lines.append(current)
                i += 1

            table = build_table(
                table_lines,
                styles
            )

            if table:
                story.append(table)
                story.append(
                    Spacer(1, 12)
                )

            continue

        # H1
        if line.startswith("# "):
            heading_text = line[2:].strip()

            if not story:
                story.append(
                    Paragraph(
                        markdown_to_reportlab(
                            heading_text
                        ),
                        styles["title"],
                    )
                )

                story.append(
                    Spacer(1, 10)
                )
            else:
                story.append(
                    Paragraph(
                        markdown_to_reportlab(
                            heading_text
                        ),
                        styles["heading1"],
                    )
                )

            i += 1
            continue

        # H2
        if line.startswith("## "):
            heading_text = line[3:].strip()

            story.append(
                Paragraph(
                    markdown_to_reportlab(
                        heading_text
                    ),
                    styles["heading1"],
                )
            )

            i += 1
            continue

        # H3
        if line.startswith("### "):
            heading_text = line[4:].strip()

            story.append(
                Paragraph(
                    markdown_to_reportlab(
                        heading_text
                    ),
                    styles["heading2"],
                )
            )

            i += 1
            continue

        # H4
        if line.startswith("#### "):
            heading_text = line[5:].strip()

            story.append(
                Paragraph(
                    markdown_to_reportlab(
                        heading_text
                    ),
                    styles["heading3"],
                )
            )

            i += 1
            continue

        # Bullet list.
        if line.startswith("- "):
            bullet_text = line[2:].strip()

            story.append(
                Paragraph(
                    "• " + markdown_to_reportlab(
                        bullet_text
                    ),
                    styles["bullet"],
                )
            )

            i += 1
            continue

        # Numbered list.
        numbered_match = re.match(
            r"^(\d+)\.\s+(.*)",
            line
        )

        if numbered_match:
            number = numbered_match.group(1)
            item = numbered_match.group(2)

            story.append(
                Paragraph(
                    f"{number}. "
                    + markdown_to_reportlab(item),
                    styles["body"],
                )
            )

            i += 1
            continue

        # Horizontal rule.
        if re.fullmatch(
            r"[-*_]{3,}",
            line
        ):
            story.append(
                Spacer(1, 8)
            )

            i += 1
            continue

        # Normal paragraph.
        paragraph_lines = [line]
        i += 1

        while i < len(lines):
            next_line = lines[i].strip()

            if not next_line:
                break

            if (
                next_line.startswith("#")
                or next_line.startswith("- ")
                or re.match(
                    r"^\d+\.\s+",
                    next_line
                )
                or "|" in next_line
            ):
                break

            paragraph_lines.append(
                next_line
            )

            i += 1

        paragraph_text = " ".join(
            paragraph_lines
        )

        story.append(
            Paragraph(
                markdown_to_reportlab(
                    paragraph_text
                ),
                styles["body"],
            )
        )

    doc.build(story)

    print(
        f"{case_id} report generated: "
        f"{output_path}"
    )

    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Usage: "
            "python scripts\\report_generator.py case-001"
        )
        sys.exit(1)

    case_id = sys.argv[1]

    if not re.fullmatch(
        r"case-\d{3}",
        case_id
    ):
        print(
            "Error: case ID must use "
            "the format case-001."
        )
        sys.exit(1)

    success = build_report(case_id)

    if not success:
        sys.exit(1)