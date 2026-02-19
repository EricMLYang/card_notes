- <https://www.edntaiwan.com/20231204ta31-bidirectional-i-o-for-communicating-power-mode-between-ecus/?fbclid=IwAR0z560Rh3vzii_1t5WyVvBDtdJhbedb-YfMkgBM67Z0g29wB5Q66cAH1cU>

- 一種單線的雙向 I/O可用於ECU之間傳送車輛電源模式，同時實現超低睡眠電流

- 近年來，汽車中的電子控制單元(ECU)數量不斷增加，同時還必需用於降低睡眠電流，以提高電池的效率。在以汽油為動力的汽車中，這已經成為強制性要求。

- 設計1無法便宜獨立控制ECU: 為了節省設計成本，汽車製造商如今會將多個ECU組合在一起並採用單個熔斷器/電子熔斷器(e-fuse)對其供電，但這會造成單獨控制ECU的缺點(圖1)。如果想要實現獨立的ON/OFF控制，那麼設計成本將會顯著增加。

- 設計2成本也高：為了克服成本問題，每個ECU都配備了來自主ECU (main MCU)的附加I/O，稱為“IGNITION” (即點火開關)。收到IGNITION輸入後，將從屬ECU (slave MCU)從睡眠狀態喚醒。這種傳統架構有其自身的局限性，例如，它需要額外的通訊介面(如LIN、CAN或乙太網路)來傳送電源模式(如睡眠、活動和其他狀態資訊)。這進一步增加了系統成本。

- 變成雙向I/O 變成硬體喚醒：

   - IGNITION是一個單向訊號，由主ECU發出，對於從屬ECU，這只是一個輸入。為了檢測此IGNITION輸入，從屬ECU中的微控制器(MCU)必須啟用喚醒源。即使ECU處於低功耗狀態，它也會消耗一些功耗以使MCU以及DC-DC控制器保持在睡眠狀態。

   - 透過將IGNITION I/O替換為硬體喚醒I/O(HW_WAKE)，圖2的基本方塊圖提出了一種具有硬體喚醒I/O的推薦架構。