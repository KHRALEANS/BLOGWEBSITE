<template>
  <div>
    <h1 class="list-title">Note List</h1>

    <ul>
      <li v-for="note in responsedata.notes" :key="note.id">
        <router-link :to="{name: 'note', params: {noteId: note.id}}">
          {{note.title}} {{getYear(note.date)}} {{getMonth(note.date)}} {{getDay(note.date)}}
        </router-link>

      </li>
    </ul>
  </div>
</template>

<script>

export default {
  name: "NoteList",
  data() {
    return {
      responsedata: {}
    }
  },
  methods: {
    async fetchApi() {
      await this.$http.get('http://localhost:5050/api/notes').then((response) => {
        this.responsedata = response.data;
      })
      .catch((error) => {
        console.log(error);
      })
    },
    getYear(date) {
      let year = date.split(' ');
      year = year[3];
      return year
    },
    getMonth(date) {
      let month = date.split(' ');
      month = month[2];
      return month
    },
    getDay(date) {
      let day = date.split(' ');
      day = day[1];
      return day
    }
  },
  mounted() {
    this.fetchApi()
  }
}
</script>

<style scoped>
.list-title {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
