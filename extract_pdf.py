#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF 文字提取工具
"""
import pdfplumber
import os
from pathlib import Path

def extract_pdf_text(pdf_path, output_path=None, max_pages=None):
    """
    從 PDF 檔案提取文字
    
    Args:
        pdf_path: PDF 檔案路徑
        output_path: 輸出文字檔案路徑（可選）
        max_pages: 最大頁數（可選，預設提取全部）
    """
    
    if not os.path.exists(pdf_path):
        print(f"❌ 檔案不存在: {pdf_path}")
        return None
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"📄 開啟 PDF: {Path(pdf_path).name}")
            print(f"📊 總頁數: {len(pdf.pages)}")
            print("-" * 50)
            
            all_text = []
            pages_to_extract = min(max_pages or len(pdf.pages), len(pdf.pages))
            
            for i, page in enumerate(pdf.pages[:pages_to_extract], 1):
                print(f"⏳ 提取第 {i}/{pages_to_extract} 頁...")
                text = page.extract_text()
                all_text.append(f"\n{'='*50}\n頁 {i}\n{'='*50}\n{text}")
            
            full_text = "\n".join(all_text)
            
            # 保存到檔案
            if output_path:
                os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(full_text)
                print(f"✅ 已保存: {output_path}")
            
            return full_text
            
    except Exception as e:
        print(f"❌ 錯誤: {e}")
        return None

def main():
    # 要提取的 PDF 檔案
    pdf_file = "曲線坐標系的處理/4.Volumetric_Lattice_Boltzmann_Models_in_General_Cur.pdf"
    output_file = "extracted_text/Volumetric_LBM.txt"
    
    print("🔍 PDF 文字提取工具\n")
    
    if os.path.exists(pdf_file):
        # 提取全部頁數
        text = extract_pdf_text(pdf_file, output_file)
        
        if text:
            print(f"\n📖 前 5 頁內容預覽（前 1000 字）:\n")
            print(text[:1000])
            print("\n...")
    else:
        print(f"❌ PDF 檔案不存在: {pdf_file}")
        print(f"\n📂 目前目錄中的 PDF 檔案:")
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith(".pdf"):
                    print(f"  - {os.path.join(root, file)}")

if __name__ == "__main__":
    main()
