---
tags:
  - system-design
  - book
---
# Building Multi-Tenant SaaS 

- Architectures Designing the database for a multi-tenant SaaS architecture involves several considerations to ensure

   - 業界規定

   - cost

   - performance: efficient data partitioning and retrieval.

   - data isolation ＆ security: prevent cross-tenant access.

   - scalability

   - plan for horizontal scaling if necessary.





## 儲存可能解法

- 獨立 DB :  特別要求 or 每一家業者都很大

- **Single Database, Separate Schemas**

   - 有數家中大型業者, data volume is significant but manageable 

   - **Benefits**:

      - Better data isolation compared to a shared schema.

      - Easier to manage operator-specific requirements and updates.

   - **Drawbacks**:

      - Increased complexity in schema management.

      - Potential for larger database size to impact performance.

- **Single Database, Shared Schema with Tenant ID**

   - 有很多家的小型業者

   - **Benefits**:

      - Lower operational costs and simpler management.

      - Easier to implement and maintain.

   - **Drawbacks**:

      - Requires strong data access controls to ensure data isolation.

      - Potential performance bottlenecks as data volume grows.


