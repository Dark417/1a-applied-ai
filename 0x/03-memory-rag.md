# Agent Memory & RAG

- [← 返回总目录](x-note.md)
- agent 记忆分层、RAG、知识库
- 共 3 篇，按收藏顺序倒序（最新在上）

## Part 1 · Index

- [Agent 记忆的 5 层架构（13 页）](#x-2114319310005150101) · @AnnatarXBT · 2026-10-25 · 概念介绍 + 数据
- [RAG Is a Lie We Tell Ourselves — Karpathy's LLM Wiki](#x-2050228936270037068) · @Suryanshti777 · 2026-05-01 · 概念对比
- [How to Master RAG and Build AI Agents That Remember Everything](#x-2050145400204783631) · @eng_khairallah1 · 2026-05-01 · 入门教程（长文）

## Part 2 · Details

### x-2114319310005150101

**Agent 记忆的 5 层架构（13 页）**

- 作者：Annatar.md (@AnnatarXBT) · 发帖 2026-10-25 · [原帖](https://x.com/AnnatarXBT/status/2114319310005150101)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：概念介绍 + 数据
- **总结**：介绍 agent 记忆的五层：working（当前窗口）、episodic（带时间戳的日志）、semantic（知识图谱里的事实）、procedural（把有效做法沉淀成 skill）、forgetting（删除过时或矛盾的信息）。用数据说明收益：Mem0 每次查询从 2.6 万 token 降到 1800，延迟降 91%；Snowflake 加一层 ontology，准确率 +20%，tool call −39%。核心观点：几乎没人做的「遗忘」层，决定了其余四层还值不值得信任。

**正文**

- **Agent memory, in 13 pages** — the fix that took one setup from 26,000 tokens per query to 1,800
- **The problem**: your agent reads the same 12 files every morning, reaches the same conclusions, and bills you again for both
- **The 5 layers that stop it**
  - **Working memory** — what it sees right now; gone once the window fills
  - **Episodic memory** — a timestamped log, so the deploy that died at 3am gets explained once
  - **Semantic memory** — facts in a knowledge graph, e.g. "this user prefers TypeScript"
  - **Procedural memory** — three approaches tried, the one that worked saved as a skill
  - **Forgetting** — what to delete before contradictions pile up
- **The numbers**
  - **Mem0** — 1,800 tokens per query instead of 26,000, with 91% lower latency
  - **Snowflake** — one ontology layer, 20% more accuracy, 39% fewer tool calls
- **The forgetting engine is the layer almost nobody builds** — and it decides whether the other four stay trustworthy
- Memory cuts what your agent reads; **Jev** cuts what it pays to decide — on the decision side it took one Claude bill from $765 to $3 a month

<details><summary>原文</summary>

> agent memory, in 13 pages
>
> the fix that took one setup from 26,000 tokens per query down to 1,800
>
> your agent reads the same 12 files every morning, reaches the same conclusions and bills you again for both
>
> the 5 layers that stop it:
> > working memory - what it sees right now, gone once the window fills
> > episodic memory - a timestamped log, so the deploy that died at 3am gets explained once
> > semantic memory - facts in a knowledge graph, like "this user prefers TypeScript"
> > procedural memory - three approaches tried, the one that worked saved as a skill
> > forgetting - what to delete before contradictions pile up
>
> the numbers:
> > Mem0 - 1,800 tokens per query instead of 26,000, with 91% lower latency
> > Snowflake - one ontology layer, 20% more accuracy, 39% fewer tool calls
>
> the forgetting engine is the layer almost nobody builds, and it decides whether the other four stay worth trusting
>
> memory cuts what your agent reads. Jev cuts what it pays to decide, and on the decision side that took one Claude bill from $765 to $3 a month 👇

</details>

- 含视频（未转写）

[↑ 回到本页目录](#part-1--index)

### x-2050228936270037068

**RAG Is a Lie We Tell Ourselves — Karpathy's LLM Wiki**

- 作者：Suryansh Tiwari (@Suryanshti777) · 发帖 2026-05-01 · [原帖](https://x.com/Suryanshti777/status/2050228936270037068)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：概念对比
- **总结**：对比 RAG 和 Karpathy 提出的 LLM Wiki。RAG 每次都从原始 chunk 重新拼答案，关掉会话就什么都没积累，没有复利。LLM Wiki 让 LLM 维护一份持久的、相互链接的 markdown wiki：每加一份文档，就读取、抽取并整合进去，更新实体页、修订摘要、标记矛盾，让知识越用越多。和你现在做的「X 收藏 → 知识库」思路直接相关。

**正文**

- **Most AI + knowledge workflows don't accumulate anything**
  - You upload documents, ask a question, and the LLM scans raw chunks to assemble an answer
  - When you close the tab, everything the system figured out disappears
  - Next session it starts from zero again — forever
- **This is RAG**
  - Powers NotebookLM, ChatGPT file uploads, and almost every "chat with your docs" product
  - It works, but has a hard ceiling: **no compounding**
  - The system doesn't get smarter about your knowledge; it keeps re-deriving the same insights
- Andrej Karpathy proposes a pattern that breaks this ceiling: **LLM Wiki**
- **Core Idea**
  - Instead of retrieving from raw documents every time, the LLM builds and maintains a **persistent wiki**
    - A structured, interlinked set of markdown files sitting between you and your sources
  - Adding a document is not just indexing — the LLM reads, extracts, and integrates it
    - Updates entity pages
    - Refines summaries
    - Flags contradictions
    - Strengthens the overall synthesis
  - **Key shift: knowledge is compiled once and continuously updated, not recreated on every query**
  - This makes the wiki a compounding system
    - Cross-references already exist
    - Contradictions are already surfaced
    - Insights evolve over time
    - Even your questions can become new pages, so exploration compounds too
- **Architecture**
  - **Raw Sources** — your documents, papers, and transcripts, left unchanged; the ground-truth layer
  - **The Wiki** — LLM-generated markdown pages (summaries, entities, concepts, comparisons, a running synthesis); the LLM maintains this layer
  - **The Schema** — a guiding config (like `CLAUDE.md` or `AGENTS.md`) defining structure, conventions, and workflows
    - Turns the LLM into a disciplined knowledge maintainer
- **How It Works in Practice**
  - **Ingestion** — adding a source triggers deep integration, not storage
    - The LLM reads it, extracts insights, writes summaries, updates multiple pages, links everything
    - One document can touch 10–15 pages
  - **Querying** — questions are answered from the wiki, not raw files
    - The LLM navigates structured knowledge and synthesizes responses
    - Valuable answers can be stored back as new pages
  - **Linting** — the system self-checks
    - Detects contradictions, outdated claims, missing links, underdeveloped concepts
    - Actively improves itself over time
- **Why This Actually Works**
  - The real bottleneck in knowledge systems isn't thinking — it's **maintenance**
    - Updating links, resolving contradictions, keeping everything consistent is tedious
  - Humans abandon systems because upkeep becomes overwhelming; LLMs don't
    - They don't forget, get bored, or avoid repetitive work
    - They can update dozens of pages instantly and consistently
    - Maintenance cost drops to near zero, so the system stays alive and reliable
  - **Your role**: curate inputs, guide thinking, ask better questions — the LLM handles everything else
- **Use Cases** (far beyond research)
  - **Personal development** — structured tracking of goals, habits, insights
  - **Deep research** — an evolving thesis built across papers and reports
  - **Reading** — chapter-by-chapter breakdowns forming a companion wiki
  - **Team knowledge** — internal systems built from meetings, chats, calls
  - Any domain where knowledge accumulates over time and needs structure
- **The Memex Moment**
  - Echoes Vannevar Bush's 1945 **Memex** — a personal knowledge system with linked ideas and associative trails
  - That vision failed on one problem: maintenance — which is now solved
- **Takeaway**
  - RAG is useful but limited: it retrieves, it doesn't learn or evolve
  - LLM Wiki is a knowledge system that compounds, improves over time, and maintains itself
  - It's not a finished product but a **pattern** — you design the structure, schema, and workflow with the LLM
  - **Stop retrieving. Start compiling.**
- Karpathy's original gist with full implementation details is on GitHub

<details><summary>原文</summary>

> 《RAG Is a Lie We Tell Ourselves — Karpathy's LLM Wiki Changes Everything》
>
> Most people's AI + knowledge workflow has a dirty secret: it doesn't actually accumulate anything.
>
> You upload your documents, ask a question, and the LLM scans raw chunks to assemble an answer. It feels productive—until you close the tab. Everything the system figured out disappears. Next session, it starts from zero again. Forever.
>
> This is RAG. It powers NotebookLM, ChatGPT file uploads, and almost every “chat with your docs” product. It works—but it has a hard ceiling: there is no compounding. The system doesn’t get smarter about your knowledge; it just keeps re-deriving the same insights again and again.
>
> Andrej Karpathy proposes a pattern that breaks this ceiling: LLM Wiki.
>
> Core Idea
>
> Instead of retrieving from raw documents every time, the LLM builds and maintains a persistent wiki—a structured, interlinked set of markdown files sitting between you and your sources.
>
> When you add a document, the LLM doesn’t just index it. It reads, extracts, and integrates it into the wiki—updating entity pages, refining summaries, flagging contradictions, and strengthening the overall synthesis.
>
> The key shift: knowledge is compiled once and continuously updated, not recreated on every query.
>
> This makes the wiki a compounding system. Cross-references already exist. Contradictions are already surfaced. Insights evolve over time. Even your questions can become new pages—so exploration compounds too.
>
> Architecture
>
> Raw Sources
> Your documents, papers, and transcripts remain unchanged. This is the ground truth layer.
>
> The Wiki
> A structured collection of LLM-generated markdown pages—summaries, entities, concepts, comparisons, and a running synthesis. The LLM maintains this layer.
>
> The Schema
> A guiding configuration (like CLAUDE.md or AGENTS.md) that defines structure, conventions, and workflows. This turns the LLM into a disciplined knowledge maintainer.
>
> How It Works in Practice
>
> Ingestion
> Adding a source triggers deep integration, not storage. The LLM reads it, extracts insights, writes summaries, updates multiple pages, and links everything together. One document can impact 10–15 pages.
>
> Querying
> Questions are answered from the wiki, not raw files. The LLM navigates structured knowledge, synthesizes responses, and can store valuable answers back into the system as new pages.
>
> Linting
> The system self-checks: detecting contradictions, outdated claims, missing links, and underdeveloped concepts. It actively improves itself over time.
>
> Why This Actually Works
>
> The real bottleneck in knowledge systems isn’t thinking—it’s maintenance. Updating links, resolving contradictions, and keeping everything consistent is tedious.
>
> Humans abandon systems because upkeep becomes overwhelming.
>
> LLMs don’t.
> They don’t forget, get bored, or avoid repetitive work. They can update dozens of pages instantly and consistently. This drops maintenance cost to near zero—so the system stays alive and reliable.
>
> Your role becomes clear: curate inputs, guide thinking, ask better questions.
> The LLM handles everything else.
>
> Use Cases
>
> This pattern applies far beyond research:
>
> Personal development: structured tracking of goals, habits, and insights
> Deep research: evolving thesis built across papers and reports
> Reading: chapter-by-chapter breakdowns forming a rich companion wiki
> Team knowledge: internal systems built from meetings, chats, and calls
> Any domain where knowledge accumulates over time and needs structure
>
> The Memex Moment
>
> The idea echoes Vannevar Bush’s 1945 vision of the Memex—a personal knowledge system with linked ideas and associative trails.
>
> That vision failed on one problem: maintenance.
>
> Now, that problem is solved.
>
> Takeaway
>
> RAG is useful, but limited. It retrieves—it doesn’t learn or evolve.
>
> LLM Wiki is different. It’s a knowledge system that compounds, improves over time, and maintains itself.
>
> It’s not a finished product—it’s a pattern. You design the structure, schema, and workflow with the LLM.
>
> That’s the real shift:
>
> Stop retrieving. Start compiling.
>
> Karpathy’s original gist with full implementation details is available on GitHub.

</details>

- 图片：[img1](https://pbs.twimg.com/media/HHPgU7KbQAA1oUv?format=jpg&name=large)

[↑ 回到本页目录](#part-1--index)

### x-2050145400204783631

**How to Master RAG and Build AI Agents That Remember Everything**

- 作者：Khairallah AL-Awady (@eng_khairallah1) · 发帖 2026-05-01 · [原帖](https://x.com/eng_khairallah1/status/2050145400204783631)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：入门教程（长文）
- **总结**：RAG 入门长文：为什么需要 RAG（模型不了解你的数据）、五阶段流水线（摄取、embedding、存储、检索、生成），给出带引用要求的 system prompt 模板，演示怎么搭第一个 RAG 应用，列出 5 个最常见的失败及修复办法，最后讲从 MVP 到生产。偏基础，适合补齐 RAG 全流程概念。

**正文**

- **The problem that kills most AI agents before production: the model does not know your data**
  - It doesn't know your company's products, documentation, or customer history
  - It doesn't know anything outside its training data
  - For most business applications, **the value lives entirely in YOUR data** — not the internet's
- **RAG (Retrieval-Augmented Generation) fixes this**
  - Gives any model access to your specific data: documents, databases, knowledge bases, wikis, transcripts
  - Lets it answer questions and complete tasks using that data as its **source of truth**
  - Without RAG, your assistant is a well-read stranger
  - With RAG, it's a colleague who has read every document your company ever produced
  - Goal of this course: build agents that answer from YOUR data, with accuracy and citations
- **What RAG actually does (in plain English)**
  - Example question: "What is our refund policy for enterprise customers?"
  - **Without RAG**: Claude doesn't know the policy → says "I do not know" or hallucinates something plausible but wrong
  - **With RAG**, the application does this:
    - **Step 1 ·** Converts the question into an **embedding** — a mathematical representation of its meaning
    - **Step 2 ·** Searches your document collection for the most relevant chunks (refund policy doc, enterprise terms of service, support guidelines)
    - **Step 3 ·** Passes those chunks to Claude along with the question
    - **Step 4 ·** Claude reads them and answers based specifically on what they say
  - Result: an accurate, grounded answer from your actual documentation, with exact citations
  - **RAG does not fine-tune or change the model at all**
    - It changes what information the model has access to at generation time
    - Like handing someone a reference book before asking a question — they don't memorize it, they look up the relevant sections
- **The RAG pipeline: 5 stages**
  - Every RAG system follows the same pipeline; understanding these stages is the foundation for building any RAG app
- **Stage 1: Document Ingestion**
  - Data lives in many formats: PDFs, Word docs, web pages, databases, spreadsheets, Slack messages, email archives
  - It must be converted into a format the system can process
  - **Ingestion process**
    - Collect source documents from wherever they live
    - Convert everything to plain text
      - PDFs → text extraction
      - Word docs → parsing
      - Web pages → HTML stripping
      - Databases → query export
    - Clean the text: remove headers, footers, navigation, and formatting artifacts that add noise without meaning
  - **Chunking — the most important decision in your entire RAG system**
    - Documents must be split into smaller chunks because:
      - Models have context limits
      - Smaller, focused chunks give more precise search results than whole documents
  - **Chunking strategies**
    - **Fixed-size** — split every 500 tokens
      - Simple, but can split mid-sentence or mid-paragraph and break meaning
    - **Semantic** — split at natural boundaries (paragraph breaks, section headers, topic transitions)
      - Preserves meaning, but chunk sizes are uneven
    - **Recursive** — try paragraphs first; if still too large, sentences; if still too large, a fixed character count
      - **Best general-purpose approach**
    - **Overlapping** — each chunk overlaps the previous by 50–100 tokens
      - Keeps information that spans a boundary from being lost
      - Slightly more storage, significantly better retrieval
  - **Sweet spot for most agents: 300–500 tokens per chunk, 50–100 tokens overlap**
    - Too small → chunks lack context
    - Too large → results get diluted with irrelevant information
- **Stage 2: Embedding**
  - Each chunk is converted into a **vector** that captures its meaning
  - Chunks on similar topics get similar vectors even with completely different words — **meaning, not just keywords**
  - **Which embedding model to use**
    - Most applications: an established model like `text-embedding-3-small` from OpenAI, or the equivalent from your provider — high quality, low cost
    - Specialized domains (medical, legal, financial): consider domain-specific models trained on that field's text
      - They understand domain vocabulary and relationships better
  - Embed every chunk and **store the vector alongside the original text**
    - Vector → for searching
    - Text → for passing to the model
- **Stage 3: Storage**
  - Chunks and vectors live in a **vector database**
  - **Options by complexity**
    - Learning / small projects: **Chroma** — open-source, runs locally, simple API
    - Production: **Pinecone, Weaviate, or Qdrant** — managed services handling scaling, backups, performance
    - Existing PostgreSQL users: **pgvector** extension — vector search in your existing DB, no separate system
  - Each record stores:
    - The original text
    - The embedding vector
    - Metadata: source document name, page number, section, date, plus any attributes useful for filtering
- **Stage 4: Retrieval**
  - Finds the most relevant chunks when a user asks a question
  - **Process**
    - Embed the question with **the same embedding model** used for the documents
    - Search for chunks whose embeddings are most similar to the question embedding
    - Return the top 3–10 chunks
  - **Improving retrieval quality**
    - **Hybrid search** — combine vector similarity with traditional keyword search
      - Some questions need semantic similarity, others exact keyword matches; hybrid covers both
    - **Metadata filtering** — filter before searching
      - Question about a specific product → only search that product's docs
      - Question about a recent policy → filter by date
      - Fewer, more relevant chunks beat more, less relevant chunks
    - **Re-ranking** — a second pass that re-orders results by relevance
      - Cross-encoder models excel here: they judge each chunk in the context of the specific question
- **Stage 5: Generation**
  - Pass the retrieved chunks to Claude with the user's question and a system prompt telling it to answer from the provided documents
  - **System prompt structure**
    ```markdown
    You are a helpful assistant that answers questions based on 
    the provided context documents. 

    Rules:
    - Answer ONLY based on information in the provided context
    - If the context does not contain enough information to answer 
      the question fully, say so explicitly
    - Cite the source document for every claim you make
    - Never make up information that is not in the context
    - If the context contains conflicting information, present 
      both perspectives and note the conflict

    Context documents:
    {retrieved_chunks}

    User question: {question}
    ```
  - **The explicit "answer only from the context" instruction is critical**
    - Without it, Claude supplements with general knowledge that may be outdated or wrong for your domain
- **Building your first RAG application (minimum viable system)**
  - Build this first, then add sophistication
  - **Step 1 ·** Collect 10–20 documents from your domain — product docs, FAQs, policies, whatever users would ask about
  - **Step 2 ·** Chunk with recursive chunking: **400-token chunks, 100-token overlap**
  - **Step 3 ·** Embed each chunk via an embedding API; store chunks and vectors in Chroma
  - **Step 4 ·** Build the retrieval function: embed the query → search Chroma for the top 5 chunks → return them
  - **Step 5 ·** Build the generation function: take retrieved chunks + question → build the prompt with the system prompt above → send to Claude
  - **Step 6 ·** Build a simple interface: a text input and an answer display (Next.js, or even a command-line interface)
  - **Step 7 ·** Test with 20 questions you know the answers to
    - Compare against correct answers
    - Identify where it fails and why
  - Takes a weekend; it won't be perfect, but it will work — every improvement from here is incremental
- **The 5 most common RAG failures (and fixes)**
  - **Failure 1: Wrong chunks retrieved** — answer is wrong or generic
    - Improve chunking: too large = irrelevant content mixed in; too small = not enough context
    - Experiment with chunk sizes
    - Add metadata filtering to narrow the search space
    - Add hybrid search to catch keyword-specific queries vector search misses
  - **Failure 2: Answer not in the retrieved chunks** — it exists in the docs but wasn't in the top results
    - Retrieve more chunks (5 → 10 or 15)
    - Add re-ranking to push the most relevant to the top
    - Check whether chunking splits the info across two chunks — if so, increase overlap
  - **Failure 3: Hallucination despite having context** — Claude presents info not in the context as if it came from your docs
    - Strengthen the system prompt; be extremely explicit:
      ```text
      Answer ONLY from the provided context. If the answer is not in the context, say 'This information is not available in the provided documents.'
      ```
    - Add a verification step where Claude quotes the specific passage behind each claim
  - **Failure 4: Duplicate chunks inflating results** — copies of the same info push out other relevant chunks
    - Deduplicate during ingestion: hash each chunk, skip duplicates
    - During retrieval, detect near-duplicates and remove them before sending to the model
  - **Failure 5: Stale data** — documents change but the vector DB still holds old versions
    - Build a refresh pipeline: re-ingest and re-embed changed documents
    - Track document versions in metadata
    - Schedule refresh cycles: daily for fast-changing content, weekly for stable content
- **From MVP to production**
  - **Authentication** — users only access documents they're authorized to see
    - Document-level access control is critical for any business application
  - **Source citations** — every answer links or references specific source documents
    - Builds trust; lets users verify
  - **Feedback collection** — users rate answers helpful / not helpful
    - Reveals which docs need better chunking, which questions fail consistently, where new documentation is needed
  - **Monitoring** — track query volume, retrieval quality, answer quality, latency, error rates
  - **Document update pipeline** — automatically detect source changes, re-process modified docs, update the vector DB
- **The bottom line**
  - **RAG is the bridge between general AI and YOUR specific domain**
    - Without it: generic answers
    - With it: answers grounded in your actual data
  - The pipeline: ingest → chunk → embed → store in a vector DB → retrieve relevant chunks per query → generate answers from them
  - Build the MVP this weekend, test it, fix the failures, add production features incrementally
  - Every business has knowledge trapped in documents nobody reads — RAG turns it into a system that answers instantly and accurately
  - Businesses that build RAG now get a knowledge advantage that compounds as they add documents

<details><summary>原文</summary>

> 《How to Master RAG and Build AI Agents That Remember Everything (Full Course)》
>
> There is one problem that kills most AI Agents before they ever reach production.
> Save this :)
> The model does not know your data.
> It does not know your company's products. It does not know your documentation. It does not know your customer history. It does not know anything that is not in its training data.
> And for most business applications, the value lives entirely in YOUR data. Not the internet's data. Yours.
> RAG (Retrieval-Augmented Generation) fixes this. It gives any AI model access to your specific data - documents, databases, knowledge bases, wikis, transcripts - and lets it answer questions and complete tasks using that data as its source of truth.
> Without RAG, your AI assistant is a well-read stranger. With RAG, it is a colleague who has read every document your company has ever produced.
> This course teaches you RAG from the ground up. By the end, you will be able to build AI Agents that answer from YOUR data with accuracy and citations.
> What RAG Actually Does (In Plain English)
> Imagine you ask Claude: "What is our refund policy for enterprise customers?"
> Without RAG, Claude does not know your refund policy. It will either say "I do not know" or hallucinate something that sounds plausible but is wrong.
> With RAG, your application does this:ƒA
> Step 1: Takes your question and converts it into a mathematical representation (an embedding) that captures its meaning.
> Step 2: Searches through your document collection to find the chunks that are most relevant to your question - your refund policy document, your enterprise terms of service, your customer support guidelines.
> Step 3: Passes those relevant chunks to Claude along with your question.
> Step 4: Claude reads the relevant documents and answers your question based specifically on what those documents say.
> The result: an accurate, grounded answer based on your actual documentation, with the ability to cite exactly where the information came from.
> RAG does not fine-tune the model. It does not change the model at all. It changes what information the model has access to at the moment it generates a response. Think of it like giving someone a reference book before asking them a question - they do not memorize the book, they look up the relevant sections.
> The RAG Pipeline: 5 Stages
> Every RAG system follows the same pipeline. Understanding these five stages is the foundation for building any RAG application.
> Stage 1: Document Ingestion
> Your data lives in many formats - PDFs, Word documents, web pages, databases, spreadsheets, Slack messages, email archives. Before RAG can use this data, it needs to be converted into a format the system can process.
> The ingestion process:
> Collect your source documents from wherever they live. Convert everything to plain text. PDFs need text extraction. Word documents need parsing. Web pages need HTML stripping. Databases need query export.
> Clean the text. Remove headers, footers, navigation elements, and formatting artifacts that add noise without adding meaning.
> Chunking - the most important decision in your entire RAG system.
> Your documents need to be split into smaller chunks because models have context limits and because smaller, focused chunks produce more precise search results than entire documents.
> Chunking strategies:
> Fixed-size chunks: Split text every 500 tokens. Simple but can split mid-sentence or mid-paragraph, breaking meaning.
> Semantic chunks: Split at natural boundaries - paragraph breaks, section headers, topic transitions. Preserves meaning but produces uneven chunk sizes.
> Recursive chunking: Try to split at paragraphs first. If a chunk is still too large, split at sentences. If still too large, split at a fixed character count. Best general-purpose approach.
> Overlapping chunks: Each chunk overlaps with the previous one by 50 to 100 tokens. Ensures that information spanning a chunk boundary is not lost. Slightly increases storage but significantly improves retrieval quality.
> The sweet spot for most Agents: 300 to 500 tokens per chunk with 50 to 100 tokens of overlap. Too small and chunks lack context. Too large and search results are diluted with irrelevant information.
> Stage 2: Embedding
> Each chunk needs to be converted into a vector - a mathematical representation that captures its meaning. This is called embedding.
> Two chunks that discuss similar topics will have similar vectors, even if they use completely different words. The embedding captures meaning, not just keywords.
> Which embedding model to use:
> For most applications, use an established embedding model like text-embedding-3-small from OpenAI or the equivalent from your preferred provider. These produce high-quality embeddings at low cost.
> For specialized domains (medical, legal, financial), consider domain-specific embedding models that are trained on text from that field. They understand domain vocabulary and relationships better than general models.
> Embed every chunk and store the vector alongside the original text. You will need both: the vector for searching, the text for passing to the model.
> Stage 3: Storage
> You need a place to store your chunks and their vectors. This is called a vector database.
> Options by complexity:
> For learning and small projects: Chroma. Open-source, runs locally, simple API, perfect for getting started.
> For production applications: Pinecone, Weaviate, or Qdrant. Managed services that handle scaling, backups, and performance optimization.
> For existing PostgreSQL users: pgvector extension. Add vector search to your existing database without deploying a separate system.
> Your vector database stores each chunk as a record with the original text, the embedding vector, and metadata (source document name, page number, section, date, and any other attributes useful for filtering).
> Stage 4: Retrieval
> When a user asks a question, the retrieval stage finds the most relevant chunks from your database.
> The process:
> Embed the user's question using the same embedding model you used for your documents. Search the vector database for the chunks whose embeddings are most similar to the question embedding. Return the top 3 to 10 most relevant chunks.
> Improving retrieval quality:
> Hybrid search: Combine vector similarity search with traditional keyword search. Some questions are best answered by semantic similarity, others by exact keyword matches. Hybrid search covers both cases.
> Metadata filtering: Before searching, filter by relevant metadata. If the user asks about a specific product, only search chunks from that product's documentation. If they ask about a recent policy, filter by date. Fewer, more relevant chunks beat more, less relevant chunks.
> Re-ranking: After the initial retrieval, run a second pass that re-ranks the results by relevance. Cross-encoder models are excellent at re-ranking because they evaluate the relevance of each chunk in the context of the specific question.
> Stage 5: Generation
> The final stage passes the retrieved chunks to Claude along with the user's question and a system prompt that instructs Claude to answer based on the provided documents.
> The system prompt structure:
> markdown
> You are a helpful assistant that answers questions based on 
> the provided context documents. 
>
> Rules:
> - Answer ONLY based on information in the provided context
> - If the context does not contain enough information to answer 
>   the question fully, say so explicitly
> - Cite the source document for every claim you make
> - Never make up information that is not in the context
> - If the context contains conflicting information, present 
>   both perspectives and note the conflict
>
> Context documents:
> {retrieved_chunks}
>
> User question: {question}
> The explicit instruction to answer only from the context is critical. Without it, Claude will supplement with its general knowledge, which may be outdated or incorrect for your specific domain.
> Building Your First RAG Application
> Here is the minimum viable RAG system. Build this first, then add sophistication.
> Step 1: Collect 10 to 20 documents from your domain. Product documentation, FAQs, policy documents - whatever your users would ask questions about.
> Step 2: Chunk the documents using recursive chunking with 400-token chunks and 100-token overlap.
> Step 3: Embed each chunk using an embedding API. Store the chunks and vectors in Chroma.
> Step 4: Build the retrieval function that embeds a query, searches Chroma for the top 5 most similar chunks, and returns them.
> Step 5: Build the generation function that takes the retrieved chunks and the user's question, constructs the prompt with the system prompt above, and sends it to Claude.
> Step 6: Build a simple interface - a text input for questions and a display area for answers. Use Next.js or even a simple command-line interface.
> Step 7: Test with 20 questions that you know the answers to. Compare the system's answers against the correct answers. Identify where it fails and why.
> This minimum system takes a weekend to build. It will not be perfect. But it will work, and every improvement you make from here is incremental.
> The 5 Most Common RAG Failures (And How to Fix Each One)
> Failure 1: Wrong chunks retrieved.
> The system returns chunks that are not relevant to the question. The answer is either wrong or generic.
> Fix: Improve your chunking strategy. If chunks are too large, they contain too much irrelevant information alongside the relevant part. If they are too small, they lack sufficient context. Experiment with chunk sizes. Add metadata filtering to narrow the search space. Implement hybrid search to catch keyword-specific queries that vector search misses.
> Failure 2: Answer not in the retrieved chunks.
> The answer exists in your documents, but the relevant chunk was not in the top results.
> Fix: Increase the number of chunks retrieved (from 5 to 10 or 15). Implement re-ranking to push the most relevant chunks to the top. Check if your chunking strategy splits the relevant information across two chunks - if so, increase overlap.
> Failure 3: Hallucination despite having context.
> Claude generates information that is not in the provided context, presenting it as if it came from your documents.
> Fix: Strengthen the system prompt. Be extremely explicit: "Answer ONLY from the provided context. If the answer is not in the context, say 'This information is not available in the provided documents.'" Add a verification step where Claude quotes the specific passage it is basing each claim on.
> Failure 4: Duplicate chunks inflating results.
> Multiple copies of the same information appear in the retrieved chunks, pushing out other relevant chunks.
> Fix: Add deduplication during ingestion. Hash each chunk and skip duplicates. During retrieval, check for near-duplicate results and remove them before sending to the model.
> Failure 5: Stale data.
> Your documents change but your vector database still contains old versions.
> Fix: Implement a refresh pipeline. When source documents are updated, re-ingest and re-embed the changed documents. Track document versions with metadata. For frequently changing data, schedule regular refresh cycles - daily for fast-changing content, weekly for stable content.
> From MVP to Production
> Your weekend RAG system works. Here is how to make it production-grade:
> Add authentication. Users should be able to create accounts and access only documents they are authorized to see. Document-level access control is critical for any business application.
> Add source citations. Every answer should include links or references to the specific source documents. This builds trust and allows users to verify information.
> Add feedback collection. Let users rate answers as helpful or not helpful. Use this feedback to identify which documents need better chunking, which questions fail consistently, and where new documentation is needed.
> Add monitoring. Track query volume, retrieval quality, answer quality, latency, and error rates. This data drives continuous improvement.
> Add a document update pipeline. When source documents change, your RAG system should automatically detect the changes, re-process the modified documents, and update the vector database.
> The Bottom Line
> RAG is the bridge between general AI and YOUR specific domain. Without it, AI gives generic answers. With it, AI gives answers grounded in your actual data.
> The pipeline is straightforward: ingest documents, chunk them, embed them, store in a vector database, retrieve relevant chunks for each query, and generate answers from those chunks.
> Build the minimum viable system this weekend. Test it. Fix the failures. Add production features incrementally.
> Every business has knowledge trapped in documents that nobody reads. RAG turns that trapped knowledge into an AI system that answers questions instantly and accurately.
> The businesses that build RAG systems now will have a knowledge advantage that compounds every day as they add more documents.
> Follow me @eng_khairallah1 for more technical deep-dives, building guides, and AI architecture breakdowns.
> hope this was useful for you, Khairallah ❤️

</details>

- 图片：[img1](https://pbs.twimg.com/media/HHMAj2rbEAALC9w?format=jpg&name=large)

[↑ 回到本页目录](#part-1--index)
