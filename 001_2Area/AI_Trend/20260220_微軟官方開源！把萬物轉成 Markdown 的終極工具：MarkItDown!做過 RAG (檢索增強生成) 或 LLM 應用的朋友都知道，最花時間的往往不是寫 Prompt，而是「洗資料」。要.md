# 微軟官方開源！把萬物轉成 Markdown 的終極工具：MarkItDown

做過 RAG (檢索增強生成) 或 LLM 應用的朋友都知道，最花時間的往往不是寫 Prompt，而是「洗資料」。要把 PDF 裡的表格、PPT 裡的圖片、Excel 裡的數據清洗成 LLM 看得懂的格式，真的會讓人崩潰。

今天要推薦微軟剛開源的神器 —— markitdown！

▌它能做什麼？ 它是一個 Python 工具 (也支援 CLI)，能將各種主流文件格式轉換為標準的 Markdown。 ✅ 支援格式：PDF, PowerPoint, Word, Excel, Images (EXIF & OCR), Audio (EXIF & 轉錄), HTML, CSV, JSON, XML... ✅ 結構保留：它不只是轉純文字，還會盡量保留標題、列表、表格等結構，這對 RAG 的分塊 (Chunking) 非常重要。

▌殺手級功能：LLM 視覺整合 這是我覺得最厲害的地方。你可以傳入 LLM client (如 GPT-4o)，當它遇到文件中的圖片或圖表時，會自動調用 AI 生成詳細的文字描述，並嵌入到 Markdown 中。

這徹底解決了以往 PDF 轉檔後「圖表資訊遺失」的痛點！

微軟官方開源！把萬物轉成 Markdown 的終極工具：MarkItDown

做過 RAG (檢索增強生成) 或 LLM 應用的朋友都知道，最花時間的往往不是寫 Prompt，而是「洗資料」。要把 PDF 裡的表格、PPT 裡的圖片、Excel 裡的數據清洗成 LLM 看得懂的格式，真的會讓人崩潰。

今天要推薦微軟剛開源的神器 —— markitdown！

▌它能做什麼？ 它是一個 Python 工具 (也支援 CLI)，能將各種主流文件格式轉換為標準的 Markdown。 ✅ 支援格式：PDF, PowerPoint, Word, Excel, Images (EXIF & OCR), Audio (EXIF & 轉錄), HTML, CSV, JSON, XML... ✅ 結構保留：它不只是轉純文字，還會盡量保留標題、列表、表格等結構，這對 RAG 的分塊 (Chunking) 非常重要。

▌殺手級功能：LLM 視覺整合 這是我覺得最厲害的地方。你可以傳入 LLM client (如 GPT-4o)，當它遇到文件中的圖片或圖表時，會自動調用 AI 生成詳細的文字描述，並嵌入到 Markdown 中。

這徹底解決了以往 PDF 轉檔後「圖表資訊遺失」的痛點！