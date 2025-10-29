<template>
  <div class="card graph-preview">
    <header>
      <h3>因果关系图谱</h3>
      <button class="btn-secondary" @click="$emit('refresh')">刷新图谱</button>
    </header>
    <div v-if="!graph" class="placeholder">暂无图谱数据</div>
    <div v-else class="graph-content">
      <section>
        <h4>节点 ({{ graph.nodes.length }})</h4>
        <div class="grid two-cols">
          <div v-for="node in graph.nodes" :key="node.id" class="node-card">
            <strong>{{ node.label }}</strong>
            <span class="chip">{{ node.category }}</span>
          </div>
        </div>
      </section>
      <section>
        <h4>关系 ({{ graph.edges.length }})</h4>
        <ul>
          <li v-for="(edge, index) in graph.edges" :key="index">
            <span>{{ edge.source }} → {{ edge.target }}</span>
            <span class="chip">{{ edge.relation || 'influences' }}</span>
            <small>权重 {{ Number(edge.weight).toFixed(1) }}</small>
          </li>
        </ul>
      </section>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  graph: {
    type: Object,
    default: null
  }
})
</script>

<style scoped>
.graph-preview header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.graph-preview h3 {
  margin: 0;
  color: #0f172a;
}

.graph-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.graph-content section h4 {
  margin: 0 0 0.75rem 0;
  color: #334155;
}

.node-card {
  background: #eef2ff;
  padding: 0.75rem;
  border-radius: 0.75rem;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.chip {
  display: inline-flex;
  align-items: center;
  padding: 0.1rem 0.6rem;
  font-size: 0.75rem;
  border-radius: 999px;
  background: #c7d2fe;
  color: #312e81;
}

.graph-content ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.5rem;
}

.graph-content li {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  background: #f1f5f9;
  padding: 0.6rem 0.8rem;
  border-radius: 0.75rem;
  align-items: center;
}

.placeholder {
  text-align: center;
  color: #94a3b8;
  padding: 2rem 0;
}
</style>
