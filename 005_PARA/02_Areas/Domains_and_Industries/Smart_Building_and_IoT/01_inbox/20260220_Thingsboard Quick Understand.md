---
tags:
  - system-design
  - data-platform
  - backend
---
# Thingsboard Quick Understand

- what?

   - an open-source IoT platform

   - enable server-side infrastructure for IoT applications

   - provide the out-of-the-box IoT cloud or on-premises solution

- Feature:

   - Get Data:

      - Provision devices, assets and customers, and define relations between them.

      - Collect and visualize data from devices and assets.

      - Push device data to other systems.

   - Check Data

      - Analyze incoming telemetry and trigger alarms with complex event processing.

      - Design dynamic and responsive dashboards and present device or asset telemetry and insights to your customers.

   - More Flow

      - Control your devices using remote procedure calls (RPC).

      - Build work-flows based on a device life-cycle event, REST API event, RPC request, etc.

      - Enable use-case specific features using customizable rule chains.

![image 36.png](./Thingsboard%20Quick%20Understand-assets/image%2036.png)

![image 37.png](./Thingsboard%20Quick%20Understand-assets/image%2037.png)

### Other IoT Platform:

- **Azure IoT solution architectures *\-* [Real-time asset tracking and management](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/real-time-asset-tracking-mgmt-iot-central)**

![image 38.png](./Thingsboard%20Quick%20Understand-assets/image%2038.png)

## Gateways

- Gateways act as intermediaries between devices and the ThingsBoard platform.

- Allows devices that might not be directly compatible with the platform to still integrate and communicate effectively.

- Bridge the communication between devices that may use different protocols (Modbus, OPC-UA, Other Protocols ) and the ThingsBoard platform.

- natively support ThingsBoard's protocols:

   - HPPT

   - MQTT

   - CoAP

   - SNMP

   - LwM2M

- Workflow

   1. Devices Communication: Devices send data to the gateway using protocols like Modbus, OPC-UA, or other specific protocols. 

   2. Protocol Translation: The gateway translates this data into a common protocol that ThingsBoard can process, such as MQTT.

   3. Forwarding Data: The translated data is then sent from the gateway to the ThingsBoard platform using the MQTT protocol.

- **IoT Gateway Architecture**

   - a software component that is designed to run on a Linux based microcomputers that support **Python 3.7+**

   - Connector:

      - The purpose is to connect to external system (e.g. MQTT broker or OPC-UA server) or directly to devices (e.g. Modbus, BLE or CAN).

      - Once connected, the connector either poll data from those systems or subscribe to updates.

   - Converter

      - Converters are responsible for converting data from protocol specific format to/from ThingsBoard format.

   - **Event Storage:** The Event Storage is used to temporary store the telemetry and other events produced by Connectors until they are delivered to ThingsBoard.

   - **ThingsBoard Client**

      - The Gateway communicates to ThingsBoard via MQTT protocol and uses API described **[here](https://thingsboard.io/docs/reference/gateway-mqtt-api/)**. ThingsBoard Client is a separate thread that polls Event Storage and delivers messages once connection to ThingsBoard is active.

   - **Gateway Service:** The Gateway Service is responsible for bootstrapping the Connectors, Event Storage and ThingsBoard Client.

- [如何將感測器資料傳送到雲端？方法和工作原理解釋](https://www.dusuniot.com/zh-TW/blog/how-to-send-sensor-data-to-cloud/)

![image 39.png](./Thingsboard%20Quick%20Understand-assets/image%2039.png)



## Thingsboard Transports

- ThingsBoard provides MQTT, HTTP and CoAP based APIs that are available for your device applications/firmware. Each of the protocol APIs are provided by a separate server component and is part of ThingsBoard “Transport Layer”.

- Each of the transport servers listed above communicates with the main ThingsBoard Node microservices using Kafka.

![image 40.png](./Thingsboard%20Quick%20Understand-assets/image%2040.png)

![image 41.png](./Thingsboard%20Quick%20Understand-assets/image%2041.png)

- **Third-party**

   - Kafka

   - Redis

   - Zookeeper

   - HAProxy**(or other LoadBalancer)**

   - **Databases**

## Message Queues

-  ThingsBoard supports multiple message queue implementations: Kafka, RabbitMQ, AWS SQS, Azure Service Bus and Google Pub/Sub. ( plan to extend this list in the future) 

- Using durable and scalable queues allow ThingsBoard to implement back-pressure and load balancing. Back-pressure is extremely important in case of peak loads.

## Rule Engine ( image a Node Red ) 

- purpose: building event-based workflows

- what: a framework include 3 main components :

   - Message: any incoming event.

   - Rule Node: a function that is executed on an incoming message.

   - Rule Chain: nodes are connected with each other with relations, so the outbound message from rule node is sent to next connected rule nodes.

- External Nodes: External Nodes used are used to interact with external systems.

   - **Azure IoT Hub Node**

   ![image 42.png](./Thingsboard%20Quick%20Understand-assets/image%2042.png)

   - **REST API Call Node:** Invoke REST API calls to the external REST server.

![image 43.png](./Thingsboard%20Quick%20Understand-assets/image%2043.png)

## Thingsboard Core

- ThingsBoard node is a core service written in Java that is responsible for handling:

   - **[REST API](https://thingsboard.io/docs/pe/reference/rest-api/)** calls;

   - WebSocket **[subscriptions](https://thingsboard.io/docs/pe/user-guide/telemetry/#websocket-api)** on entity telemetry and attribute changes;

   - Processing messages via **[rule engine](https://thingsboard.io/docs/pe/user-guide/rule-engine-2-0/re-getting-started/)**;

   - Monitoring device **[connectivity state](https://thingsboard.io/docs/pe/user-guide/device-connectivity-status/)** (active/inactive).

## Thingsboard Integrations

![image 44.png](./Thingsboard%20Quick%20Understand-assets/image%2044.png)

ThingsBoard Platform integrations feature was designed for two primary use cases / deployment options:

- Connect existing NB IoT, LoRaWAN, SigFox and other devices with specific payload formats directly to ThingsBoard platform.

- Stream data from devices connected to existing IoT Platforms to enable real-time interactive dashboards and efficient data processing.