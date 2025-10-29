<template>
  <div class="view">
    <header>
      <h2>生态能力构建</h2>
      <p>梳理开源技术、组织与社区的关系网络，构建完整的生态全景图。</p>
    </header>

    <div class="grid two-cols">
      <div class="card">
        <h3>生态组织与社区</h3>
        <ul class="ecosystem-list">
          <li v-for="item in ecosystemItems" :key="item.id">
            <div>
              <strong>{{ item.title }}</strong>
              <p>{{ item.summary }}</p>
              <small>影响力：{{ item.impact }}</small>
            </div>
            <div class="relations">
              <span v-for="relation in item.relations" :key="relation" class="chip">{{ relation }}</span>
            </div>
          </li>
        </ul>
      </div>

      <InsightCard title="生态洞察" :items="ecosystemInsights" />
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useIntelligenceStore } from '../stores/useIntelligenceStore'
import InsightCard from '../components/InsightCard.vue'

const store = useIntelligenceStore()

const ecosystemItems = computed(() =>
  store.items.filter((item) => item.category.toLowerCase().includes('ecosystem'))
)

const ecosystemInsights = computed(() => {
  const section = store.report?.sections?.find((section) => section.title === 'Ecosystem')
  return section?.insights || []
})

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
.ecosystem-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1rem;
}

.ecosystem-list li {
  display: grid;
  gap: 0.5rem;
  padding: 0.75rem;
  border-radius: 0.75rem;
  border: 1px solid #e2e8f0;
  background: #f8fafc;
}

.ecosystem-list p {
  margin: 0.35rem 0;
  color: #64748b;
}

.relations {
  display: flex;
  gap: 0.35rem;
  flex-wrap: wrap;
}

.chip {
  display: inline-flex;
  padding: 0.1rem 0.5rem;
  border-radius: 999px;
  background: #bbf7d0;
  color: #166534;
  font-size: 0.75rem;
}
</style>
