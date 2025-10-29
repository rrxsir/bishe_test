<template>
  <div class="view">
    <header>
      <h2>技术趋势监测</h2>
      <p>实时跟踪开源领域的新兴技术动向，识别前沿发展趋势。</p>
    </header>

    <div class="grid two-cols">
      <InsightCard title="趋势洞察" :items="trendInsights">
        <template #action>
          <button class="btn-secondary" @click="store.loadReport">刷新分析</button>
        </template>
      </InsightCard>

      <div class="card">
        <h3>趋势事件列表</h3>
        <ul class="event-list">
          <li v-for="item in trendItems" :key="item.id">
            <div>
              <strong>{{ item.title }}</strong>
              <p>{{ item.summary }}</p>
            </div>
            <span>{{ formatDate(item.timestamp) }}</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useIntelligenceStore } from '../stores/useIntelligenceStore'
import InsightCard from '../components/InsightCard.vue'

const store = useIntelligenceStore()

const trendItems = computed(() =>
  store.items.filter((item) => item.category.toLowerCase().includes('trend'))
)

const trendInsights = computed(() => {
  const trendSection = store.report?.sections?.find((section) => section.title === 'Trend')
  return trendSection?.insights || []
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

.event-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1rem;
}

.event-list li {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
}

.event-list strong {
  display: block;
  margin-bottom: 0.25rem;
}

.event-list p {
  margin: 0;
  color: #64748b;
}
</style>
