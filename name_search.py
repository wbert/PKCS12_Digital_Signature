from typing import Any, Dict, Optional, List
from pdfminer.layout import LTTextBoxHorizontal


def find_word_bbox(layout, search_word, depth=0, page_num=None) -> Optional[List[Any]]:
    """Find the bounding box of all instances of a specific word in LTTextBoxHorizontal items"""
    results = []

    for o in layout:
        if hasattr(o, "get_text") and callable(o.get_text):
            text = o.get_text().strip()
            if search_word.lower() in text.lower():
                if isinstance(o, LTTextBoxHorizontal):
                    for line in o:
                        line_text = line.get_text().strip()
                        if search_word.lower() in line_text.lower():
                            results.append(o.bbox)

    return results


def get_optional_bbox(o: Any) -> Optional[Dict[str, float]]:
    """If bounding box of LTItem if available, otherwise None"""
    if hasattr(o, "bbox"):
        x0, y0, x1, y1 = o.bbox
        return {"x0": x0, "y0": y0, "x1": x1, "y1": y1}
    return None


def generate_results(pages, search_word):
    """
    Formats the result in a dict
    PARAMETERS
    - pages: int, number of pages of the document
    - search_word: str, the word trying to search in the document
    """
    all_results = []
    for i, layout in enumerate(pages):
        results = find_word_bbox(layout, search_word, page_num=i)
        if results:
            all_results.append(
                {
                    "page_no": i,
                    "bbox": [
                        {"x0": bbox[0], "y0": bbox[1], "x1": bbox[2], "y1": bbox[3]}
                        for bbox in results
                    ],
                }
            )

    if all_results:
        print(all_results)
        return all_results
    else:
        print(f"'{search_word}' not found in the document.")
        return []
