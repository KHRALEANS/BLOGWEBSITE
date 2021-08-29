<template>
  <h2>This is the home</h2>
  <MarkdownDisplay :markdown="markdown"></MarkdownDisplay>
  <p>end of home</p>
</template>

<script>
import MarkdownDisplay from "@/components/MarkdownDisplay";
import markdown from "../data/data"

export default {
  name: "Home",
  components: {
    MarkdownDisplay
  },
  data() {
    return {
      markdown
    }
  }
}
</script>

<style scoped>

</style>
