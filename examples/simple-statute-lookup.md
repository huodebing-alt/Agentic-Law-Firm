# Example: simple statute lookup

User: 帮我查一下 民法典 关于不安抗辩权的规定。

Routing:
1. `task-router` identifies this as a research query, language `zh-CN`.
2. Dispatches to `research-statute-cn` agent.
3. `research-statute-cn` invokes the `statute-lookup` skill, which
   queries the `statutes-rag` MCP.
4. MCP returns 《民法典》第五百二十七条 (不安抗辩权) plus related
   articles.
5. `research-statute-cn` summarises and returns to `task-router`.
6. `task-router` returns the answer in Chinese.

No hard gate triggered. No fresh-context decomposition needed.

Expected wall-clock time: 5-15 seconds.
