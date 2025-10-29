<template>
  <div class="card insight-card">
    <header>
      <h3>{{ title }}</h3>
      <slot name="action"></slot>
    </header>
    <ul>
      <li v-for="(item, index) in items" :key="index">
        <slot name="item" :item="item">
          {{ item }}
        </slot>
      </li>
    </ul>
  </div>
</template>

<script setup>
const props = defineProps({
  title: {
    type: String,
    required: true
  },
  items: {
    type: Array,
    default: () => []
  }
})
</script>

<style scoped>
.insight-card header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.insight-card h3 {
  margin: 0;
  font-size: 1.1rem;
  color: #0f172a;
}

.insight-card ul {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.75rem;
}

.insight-card li {
  line-height: 1.5;
  color: #475569;
}
</style>
