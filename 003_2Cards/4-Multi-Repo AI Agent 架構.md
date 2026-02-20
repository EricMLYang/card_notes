---
tags:
  - ai-coding
  - architecture
---
# Multi-Repo AI Agent 架構

## 類型
系統架構、AI Agent

## 概念
Meta AI 團隊的經驗：在大型組織中，Multi-repo 架構搭配 AI Agent 更有效。每個 Repo 作為一個工作單元 (Worker Unit)，AI Agent 在各 Repo 中獨立運作，透過明確的 API 契約協作。優勢：(1) 隔離性——一個 Agent 出錯不影響全局；(2) 專業化——每個 Agent 專注一個領域；(3) 可擴展——新增 Agent 不影響現有系統。這種架構對應 Conway's Law：系統結構反映組織結構。

## 重要性
提供大規模 AI 代理部署的架構參考。

## 邊界
適用於大型組織；小團隊可能過度設計。

## 標籤
#ai-coding #architecture #multi-repo #agent #meta
