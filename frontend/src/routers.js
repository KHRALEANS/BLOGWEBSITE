import {createRouter, createWebHistory} from 'vue-router'
import Home from './components/Home'
import NoteList from "@/components/NoteList";
import Note from "@/components/Note";



const routes = [
    {
        path:'/list',
        name:'list',
        component:NoteList
    },

    {
        path:'/',
        name:'home',
        component:Home
    },

    {
        path:'/note/:noteId',
        name:'note',
        component: Note
    }
]


const router = createRouter({
    history:createWebHistory(),
    routes
})


export default router;
