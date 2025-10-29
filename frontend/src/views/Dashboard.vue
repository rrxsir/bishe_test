<template>
  <section class="grid two-cols">
    <DataSourceSelector
      :loading="store.loading"
      :last-updated="store.lastUpdated"
      :error="store.error"
      @refresh="handleRefresh"
    />
    <InsightCard title="关键高光" :items="store.report?.highlights || []">
      <template #action>
        <button class="btn-secondary" @click="store.loadReport">刷新分析</button>
      </template>
    </InsightCard>
  </section>

  <GraphPreview :graph="store.graph" @refresh="store.loadGraph" />
</template>

<script setup>
import { onMounted } from 'vue'
import DataSourceSelector from '../components/DataSourceSelector.vue'
import InsightCard from '../components/InsightCard.vue'
import GraphPreview from '../components/GraphPreview.vue'
import { useIntelligenceStore } from '../stores/useIntelligenceStore'

const store = useIntelligenceStore()

const handleRefresh = async (sources) => {
  await store.refreshData(sources)
  await Promise.all([store.loadReport(), store.loadGraph()])
}

onMounted(async () => {
  await store.loadData()
  if (!store.items.length) {
    await handleRefresh(['web', 'local', 'config'])
  } else {
    await Promise.all([store.loadReport(), store.loadGraph()])
  }
})
</script>

<style scoped>
section {
  align-items: stretch;
}
</style>
