<template>
  <h2>This is a note with id={{ $route.params.noteId }}</h2>
  <MarkdownDisplay :markdown="notecontent.toString()"></MarkdownDisplay>
</template>

<script>
import MarkdownDisplay from "@/components/MarkdownDisplay";

export default {
  name: "Note",
  components: {
    MarkdownDisplay
  },
  data() {
    return {
      notecontent: {}
    }
  },
  methods: {
    async loadFile() {
      await this.$http.get('http://localhost:5050/api/note/3').then((response) => {
        this.notecontent = response.data;
      })
      .catch((error) => {
        console.log(error);
      })
    }
  },
  mounted() {
    this.loadFile()
  }
}
</script>

<style scoped>

</style>
