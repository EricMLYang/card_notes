---
tags:
  - charging-master
---
# Dashboard data

## Question

- 

   ![image 61.png](./Dashboard%20data-assets/image%2061.png)

   

   

- Take Each Connection Status : 

- `repo_char_ac_sess._execute_query('''`

   `SELECT connector_id, id_tag, power, soc, ``MAX(created_at)`` AS created_at `

   `FROM ``charging_active_sessions``  `

   `WHERE created_at >= '2024-07-19'`

   `GROUP BY ``connector_id, id_tag, power, soc``; `

   `''')`

![image 62.png](./Dashboard%20data-assets/image%2062.png)

![image 63.png](./Dashboard%20data-assets/image%2063.png)







-  `charging_connectors``.id `IN  (`charging_active_sessions.connector_id`)

- In `charging_connectors`  If Change Status, No Insert, Just Update?

![image 64.png](./Dashboard%20data-assets/image%2064.png)

![image 65.png](./Dashboard%20data-assets/image%2065.png)

![image 66.png](./Dashboard%20data-assets/image%2066.png)



- take: `label`    `charging_active_sessions.``box_id`  = `charging_boxes.``id`

- status is same with connitor status?

![image 67.png](./Dashboard%20data-assets/image%2067.png)

take: `plate_number`    `charging_active_sessions.``id_tag`  = `buses.``evccid`





### `log_station_charging_daily`

![image 68.png](./Dashboard%20data-assets/image%2068.png)

## < Real Time Monitor >

![image 69.png](./Dashboard%20data-assets/image%2069.png)

- In General: `status`  from `charging_boxes`

   ![image 70.png](./Dashboard%20data-assets/image%2070.png)

- New Connection ( Bus - Pile ) :

   - `charging_active_sessions ` : Check New Data

   - take: `power`  initial KW;    take: `soc` initial Battery %

   - take: `plate_number`    `charging_active_sessions.``id_tag`  = `buses.``evccid`

   - take: `label`    `charging_active_sessions.``box_id`  = `charging_boxes.``id`

   - take: `status`    `charging_active_sessions.``connector_id`  = `charging_connectors.``id`

![image 71.png](./Dashboard%20data-assets/image%2071.png)

- Charging: Keep Track  `charging_active_sessions`  ?   

- End: `charging_completed_sessions`: Check New Data AND Take `session_id`

- 剩餘時間 ( 兩個時間相減 )：

   - `charging_active_sessions.``elapsed_time`` `

   - `charging_schedules.``estimated_completed_at` 


