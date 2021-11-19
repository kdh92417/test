axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';


const Todo = {
    delimiters: ['[[', ']]'],
    data() {
        return {
            vm: 'Hello',
            name: '',
            todo: '',
            todoList: []
        }
    },
    created: function() {
        console.log("created()...");
    },
    methods: {
        fetch_all_todo: function() {
            console.log("fetch_all_todo()...");

            let todo = this;
            axios.get('/api/todo/list/')
                .then(function (res) {
                    console.log("Get the RES", res);
                    todo.todoList = res.data;
                })
        },
        add_todo: function() {
            console.log("add_todo()...");
            if (this.todo == '') return;
            if (this.name == '') this.name = '홍길동';

            let todo = this;
            let postData = {name: this.name, todo: this.todo};
            console.log(postData, typeof postData)
            axios.post('/api/todo/create/', postData)
                .then(function (res) {
                    console.log("POST RES", res);
                    todo.todoList.push({id: res.data.id, name: res.data.name, todo: res.data.todo});
                })
                .catch(function (err) {
                    console.log("POST ERR", err);
                })
            this.name = this.todo = '';
        },
        remove_todo: function(todo, index) {
            console.log("remove_todo()...");
            if (confirm("Really delete") == false) return;

            let vm = this;
            axios.delete('/api/todo/' + todo.id + '/delete/')
                .then(function (res){
                    console.log("DELETE RES", res);
                    vm.todoList.splice(index, 1);
                })
                .catch(function (err) {
                    console.log("DELETE ERR", err);
                })
        }
    }
}

Vue.createApp(Todo).mount('#app')