import xml.etree.ElementTree as ET

def parse_law_xml(xml_content, search_word):
    root = ET.fromstring(xml_content)
    results = []

    for article in root.findall(".//조문단위"):
        article_number = article.findtext("조문번호", default="")
        article_title = article.findtext("조문제목", default="").strip()
        article_text = article.findtext("조문내용", default="").strip()

        # 불필요한 반복 제거
        if article_text.startswith(f"제{article_number}조") and article_title in article_text:
            display_text = f"제{article_number}조({article_title})"
        else:
            display_text = article_text

        matched = False
        paragraphs = []
        항목들 = article.findall("항")
        if not 항목들:
            if search_word in article_text:
                matched = True
                paragraphs.append(f"{display_text} {article_text}")
        else:
            for idx, 항 in enumerate(항목들):
                항번호 = 항.findtext("항번호", default="").strip()
                항내용 = 항.findtext("항내용", default="").strip()
                if search_word in 항내용:
                    matched = True
                    if idx == 0:
                        paragraphs.append(f"{display_text} {항번호} {항내용}")
                    else:
                        paragraphs.append(f"  {항번호} {항내용}")

                for 호 in 항.findall("호"):
                    호번호 = 호.findtext("호번호", default="").strip()
                    호내용 = 호.findtext("호내용", default="").strip()
                    if search_word in 호내용:
                        matched = True
                        paragraphs.append(f"  {호번호} {호내용}")

                    for 목 in 호.findall("목"):
                        목번호 = 목.findtext("목번호", default="").strip()
                        목내용 = 목.findtext("목내용", default="").strip()
                        if search_word in 목내용:
                            matched = True
                            paragraphs.append(f"  {목번호} {목내용}")

        if matched:
            results.append({
                "조문번호": f"제{article_number}조",
                "조문제목": article_title,
                "내용": paragraphs
            })

    return results