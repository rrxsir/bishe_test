<template>
  <div class="card data-source-selector">
    <header>
      <h3>数据源管理</h3>
      <button class="btn-primary" @click="triggerRefresh" :disabled="loading">
        {{ loading ? '同步中...' : '刷新数据' }}
      </button>
    </header>
    <p class="description">从不同的数据源采集信息，构建统一的因果知识库。</p>
    <div class="sources">
      <label v-for="source in availableSources" :key="source.value" class="source-option">
        <input type="checkbox" v-model="selected" :value="source.value" />
        <div>
          <strong>{{ source.label }}</strong>
          <p>{{ source.description }}</p>
        </div>
      </label>
    </div>
    <footer v-if="lastUpdated" class="footer">
      <small>最近更新：{{ formatDate(lastUpdated) }}</small>
    </footer>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  loading: Boolean,
  lastUpdated: String,
  error: String
})

const emit = defineEmits(['refresh'])

const availableSources = [
  {
    value: 'web',
    label: 'Web信号源',
    description: '来自公开网络与社区的实时信号'
  },
  {
    value: 'local',
    label: '本地情报库',
    description: '内部整理的重点开源项目与事件'
  },
  {
    value: 'config',
    label: '用户配置源',
    description: '自定义的重点关注对象与合作组织'
  }
]

const selected = ref(availableSources.map((source) => source.value))

watch(
  () => props.loading,
  (loading) => {
    if (!loading && selected.value.length === 0) {
      selected.value = availableSources.map((source) => source.value)
    }
  }
)

const formatDate = (value) => new Date(value).toLocaleString()

const triggerRefresh = () => {
  emit('refresh', selected.value)
}
</script>

<style scoped>
.data-source-selector header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.description {
  margin-top: 0;
  color: #64748b;
}

.sources {
  display: grid;
  gap: 0.75rem;
  margin: 1rem 0;
}

.source-option {
  display: flex;
  gap: 0.75rem;
  align-items: flex-start;
  padding: 0.75rem;
  border-radius: 0.75rem;
  border: 1px solid #e2e8f0;
  background: #f8fafc;
}

.source-option p {
  margin: 0.35rem 0 0;
  color: #64748b;
}

.footer {
  margin-top: 1rem;
  color: #94a3b8;
}

.error {
  margin-top: 0.75rem;
  color: #dc2626;
}
</style>
