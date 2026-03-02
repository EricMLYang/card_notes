---
tags:
  - automotive-pm
---
# AI & Car

## 0\. Trend 

- Smart Cockpit 是車廠重要差異化，很多功能被中國車廠發展成基礎配備

- 汽車：電動化、網聯化、智能化、共享化

- 功能特點：

   - 透過厲害的意圖辨識模型來讓操作 UI 便利性極大化

   - Multi-Activate Interaction

- 系統：

   - 計算要求越來越高：

   - 車載系統：QNX、Android、Linux 

   - 開發：

      - 制定型：從 OS 内核

- 以上都是大型語言模型有機會協助範圍

   - 可靠性？

jijji



## 1\. Industry Transformation: Software Define Vehicle

- Just like DDD or Micro-Service in System Design - Want to face customer application

   - 整合多領域的應用 ( ADAS Start the Transformation )

      - Dog Model: 購物時留狗在車上 ( 整合資訊監控、空調、電力監控…）

   - 提升軟體服務價值

![image 7.png](./AI%20&%20Car-assets/image%207.png)

- 其他好處：降低複雜度，降低成本

![image 8.png](./AI%20&%20Car-assets/image%208.png)



## 2 EV is perfect to Zonal but Fuel Car still can be improved  

Traditional fuel vehicles use a distributed ECU model, where each function (engine control, ABS, etc.) often has a separate dedicated ECU. However, modern fuel vehicles can still incorporate zone-like concepts for certain subsystems:

- **Body Control Module (BCM):** Many vehicles consolidate functions like lighting, power windows, mirrors, and HVAC systems into a central BCM, somewhat resembling a zone approach.

- **Domain Controllers:** Some vehicles move towards using domain controllers, where several closely related functionalities (e.g., powertrain domain) are managed by a single powerful controller. This is a step toward zonal architectures though not a full-fledged implementation.

- **Sensor Fusion:** For driver assistance features, modern fuel vehicles might pool data from multiple sensors (cameras, radar, etc.) into a central unit, creating a mini 'perception zone' of sorts.





## 3\. SDV and AI

-  AI is disruptive on many levels, and the automotive world is no exception. So, do we need an “AI-defined vehicle” instead of (or in addition) to a software-defined one? Where in the SDV architecture does AI play a role? The answer is: potentially in all the layers of the SDV architecture (see ++[Figure 3-8](https://learning.oreilly.com/library/view/the-software-defined-vehicle/9781098157814/ch03.html#fig_8__sdv_and_ai)++).

![image 9.png](./AI%20&%20Car-assets/image%209.png)





## 4\. High-Performance-Computer in CAR

- Traditional MCU+ECU :  ( each domain / Centralized Domain)

- ECU + SoC:  (  Zonal Domain Controller / Zonal Central Computer )

   - AUO + Qualcomm Snapdragon

- Nvidia Jetson AGX :  AI Application need more GPU?

![image 10.png](./AI%20&%20Car-assets/image%2010.png)

![image 11.png](./AI%20&%20Car-assets/image%2011.png)



## 5 Example: SoC in Car

較新的燃油車採用 SoC 的用途通常包括：

- **發動機控制**：SoC 可用於控制發動機的噴射、點火、正時和其他功能。這可以提高燃油效率、降低排放和改善性能。

   - **英飛凌 AURIX TC397 SoC** 用於發動機和變速箱控制在多種梅賽德斯-奔馳車型中，包括 C-Class、E-Class 和 S-Class。

- **變速箱控制**：SoC 可用於控制變速箱的換檔、扭矩管理和其他功能。這可以提高燃油效率、改善換檔平順性和提高性能。

- **車身控制**：SoC 可用於控制車身穩定性控制、牽引力控制、防抱死制動和其他功能。這可以提高安全性並改善操控性。

   - **恩智浦 S32K344 SoC** 用於車身控制在多種本田車型中，包括思域、雅閣和 CR-V。

- **信息娛樂**：SoC 可用於為信息娛樂系統提供動力，包括音頻、視頻、導航和其他功能。這可以提供更好的用戶體驗和更豐富的功能。

   - **德州儀器 TDA4VM SoC** 用於信息娛樂在多種通用汽車車型中，包括凱迪拉克 CT6、雪佛蘭 Silverado 和 GMC Sierra。

EV: 特斯拉較新的車型，例如 Model 3 和 Model Y，使用 **三個** SoC：

- **主 SoC:** 負責車輛的動力系統、車身控制系統、信息娛樂系統等。

- **Autopilot SoC:** 負責車輛的自動駕駛功能。

- **安全 SoC:** 負責車輛的安全功能。





## 6 Example: Nvidia AGX in Car

- <https://www.nvidia.com/en-us/self-driving-cars/> 

![image 10.png](./AI%20&%20Car-assets/image%2010.png)



## Other Player

1. **Chip Manufacturers:** Designing the hardware on which SDV software runs.

   - Qualcomm: Leading player with their Snapdragon Digital Chassis.

   - NVIDIA: Provides high-powered processors and the Omniverse platform with simulation capabilities.

   - Intel/Mobileye: Offer computer vision and self-driving solutions.

2. **Traditional OEMs:** Many car companies are developing in-house SDV capabilities alongside partnerships

   - **Hyundai**: Introduced its high-performance vehicle computer (HPVC) and SDV OS, showcasing their efforts in consolidating various vehicle functions into a single unit to enhance computation power and streamline hardware requirements. They also emphasized the importance of data-driven learning systems and safety-designed vehicles

   - General Motors: Ultifi platform.

   - Volkswagen: CARIAD software division.

   - Stellantis: Developing a range of software solutions.

3. **Tier-1 Suppliers:** Companies that traditionally provided car components now focus heavily on SDV software elements.

   - Bosch: Comprehensive middleware and software solutions.

   - Continental: Offers software solutions for vehicle domains, and high-performance computing.

   - Aptiv: Focuses on autonomous driving and connectivity software.

4. **Tech Giants:** Their expertise in software, cloud computing, and AI are crucial for SDVs.

   - Amazon Web Services (AWS): Provides cloud infrastructure and AI tools for SDV development.

   - Google/Android: Android Automotive offers potential for integration.

   - Microsoft: Their Azure cloud platform and tools play a role.

5. **Software Specialists:** Companies focused on specific SDV aspects.

   - Blackberry (QNX): Real-time operating systems for safety-critical functions.

   - Wind River: Embedded software and solutions.

At CES 2024, a range of companies unveiled or updated their SDV technologies, emphasizing the integration of complex, continuously updatable features, and support for higher levels of autonomy【6†source】. Below are the main players and their contributions to the SDV framework:

1. **Marelli**: Utilizes Qualcomm’s Snapdragon Cockpit Platform to offer a "Software-Defined Interior experience." Their zonal architecture replaces fixed analog interfaces with dynamic displays and content, showcasing an updated panorama HUD with 3D hologram virtual assistants and other innovations【6†source】.

2. **RTI**: Presented its Connext Drive middleware communication framework, already in use by over two dozen OEMs for running zonal, ADAS, and telematics architectures in SDVs. The platform is compatible with various automotive software standards and is ISO26262 ASIL-D certified【6†source】.

3. **Stradvision**: Announced improvements to its next-generation 3D Perception Network, aimed at reducing CPU usage and enhancing NPU utilization for ADAS functions, marking an optimization critical for the SDV era【6†source】.

4. **Sibros**: Demonstrated its Deep Connected Platform, aiming to power the future of software-defined mobility【6†source】.

5. **Intel**: Unveiled its first SDV System on Chip (SoC) family designed for the automotive market, featuring scalable SoCs with up to 12 cores and integrated Arc Xe graphics, highlighting their aim to cater to the AI-driven EV market【7†source】.

6. **IBM**: Discussed the role of AI and data platforms in SDVs, highlighting how generative AI can enhance SDV development and operation. IBM's Edge Application Manager and Embedded Automotive Platform are key components of their offering, aimed at improving developer productivity and vehicle operation【8†source】.

7. **AUTOCRYPT**: Focused on automotive cybersecurity for SDVs, emphasizing the necessity of dedicated communication protocols and a centralized E/E architecture to support the increasing complexity and security demands of modern vehicles【9†source】.

8. **LG Electronics and Magna**: Demonstrated a new cross-domain platform developed collaboratively, aimed at advancing automotive display technologies and optimizing screens for SDVs