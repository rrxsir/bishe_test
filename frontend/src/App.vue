<template>
  <div class="app-shell">
    <header class="app-header">
      <div class="branding">
        <h1>Causal Intelligence Hub</h1>
        <p>基于因果图的多智能体协同开源情报分析系统</p>
      </div>
      <nav class="navigation">
        <RouterLink to="/">总览</RouterLink>
        <RouterLink to="/trends">技术趋势</RouterLink>
        <RouterLink to="/projects">项目追踪</RouterLink>
        <RouterLink to="/ecosystem">生态全景</RouterLink>
      </nav>
    </header>

    <main class="app-main">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
</script>

<style scoped>
.app-shell {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1.5rem 4rem;
}

.app-header {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.branding h1 {
  margin: 0;
  font-size: 1.8rem;
  color: #1f2937;
}

.branding p {
  margin: 0.25rem 0 0;
  color: #64748b;
}

.navigation {
  display: flex;
  gap: 1rem;
  font-weight: 600;
}

.navigation a {
  padding: 0.4rem 0.75rem;
  border-radius: 999px;
  color: #1e293b;
}

.navigation a.router-link-active {
  background: #2563eb;
  color: white;
  box-shadow: 0 10px 20px rgba(37, 99, 235, 0.2);
}

.app-main {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

@media (max-width: 640px) {
  .app-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .navigation {
    width: 100%;
    flex-wrap: wrap;
  }
}
</style>
