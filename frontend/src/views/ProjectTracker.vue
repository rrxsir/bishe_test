<template>
  <div class="view">
    <header>
      <h2>开源项目追踪</h2>
      <p>持续监控重点开源项目的演进与活跃度，及时掌握关键变化。</p>
    </header>

    <div class="card">
      <table>
        <thead>
          <tr>
            <th>项目</th>
            <th>摘要</th>
            <th>影响力</th>
            <th>关联</th>
            <th>时间</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in projectItems" :key="item.id">
            <td>
              <strong>{{ item.title }}</strong>
            </td>
            <td>{{ item.summary }}</td>
            <td>{{ item.impact }}</td>
            <td>
              <span v-for="relation in item.relations" :key="relation" class="chip">{{ relation }}</span>
            </td>
            <td>{{ formatDate(item.timestamp) }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <InsightCard title="项目洞察" :items="projectInsights" />
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useIntelligenceStore } from '../stores/useIntelligenceStore'
import InsightCard from '../components/InsightCard.vue'

const store = useIntelligenceStore()

const projectItems = computed(() =>
  store.items.filter((item) => item.category.toLowerCase().includes('project'))
)

const projectInsights = computed(() => {
  const section = store.report?.sections?.find((section) => section.title === 'Project')
  return section?.insights || []
})

const formatDate = (value) => new Date(value).toLocaleDateString()

onMounted(async () => {
  if (!store.items.length) {
    await store.loadData()
  }
  if (!store.report) {
    await store.loadReport()
  }
})
</script>

<style scoped>
.view header h2 {
  margin: 0;
  color: #0f172a;
}

.view header p {
  color: #475569;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

thead {
  background: #eef2ff;
}

th,
td {
  padding: 0.75rem;
  text-align: left;
  border-bottom: 1px solid #e2e8f0;
}

.chip {
  display: inline-flex;
  padding: 0.1rem 0.5rem;
  margin-right: 0.35rem;
  border-radius: 999px;
  background: #cbd5f5;
  color: #1e1b4b;
  font-size: 0.75rem;
}
</style>
