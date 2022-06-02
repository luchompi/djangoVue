const app = new Vue({
  el:'#app',
  delimiters:['{$','$}']
  data: {
    queryset =[],
  },watch:{
    valores:function(){
      this.getData();
    }
  }
  ,
  methods:{
    getData:function(){
      var self = this;
      axios.get('htttp://127.0.0.1:8000/empresa/api/v1.0')
      .then(funcion(response){
        self.queryset=response.data
      })
      .catch(function(error){
        console.log(error);
      })

    },
  }
})
