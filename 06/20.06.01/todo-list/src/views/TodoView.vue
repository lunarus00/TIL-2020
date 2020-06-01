<template>
  <div>
      <TodoList :todos="todos"/>
      <TodoInput/>
  </div>
</template>

<script>

import TodoList from '@/components/TodoList.vue'
import TodoInput from '@/components/TodoInput.vue'

export default {
    name: 'TodoView',
    components: {
        TodoList,
        TodoInput,
    },
    data() {
        return {
            todos: [
                {
                    id: 1,
                    content: 'Django 복습',
                    isCompleted: true,
                },
                {
                    id: 2,
                    content: 'JavaScript 복습',
                    isCompleted: false,
                },
                {
                    id: 3,
                    content: 'Vue.js 학습',
                    isCompleted: false,
                },
            ]
        }
    }
}
</script>

<style>

</style>