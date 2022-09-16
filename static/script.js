'use_strict';
var root = {
	data() 
	{
	return {
		params: ['param_1','param_2','param_3','param_4','param_5','param_6','param_7','param_8'],
      	values: [],
      	result: '',
      	app_style: {
        	fontFamily: 'FontAwesome' 
        	}
		}
	},//data
	delimiters: ['{(', ')}'],
	computed: {
		class_res () {
        	if ('' == this.result)
        		return 'd-none';
          	else if (isNaN(this.result*1))
              return 'alert alert-danger';
          	return 'alert alert-success';
        }
		
	},//computed
	
	methods: {
      get_pred(){
        if (this.values.length != this.params.length){
          alert('Введите все параметры!');
          return ; 
        }
        (async () => {
        const rawResponse = await fetch('/api', {
          method: 'POST',
          headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.values)
        });
        try{
        	const content = await rawResponse.json();
          	this.result = this.parse_res(content);
            console.log(content, typeof content);
        } catch(e){
          this.result = 'Ошибка сервиса'
        }
          
       })();
      },//get_pred
	   parse_res (data) {
			let a = 1*data;
         	if (-1 == a) return 'Данные вне диапазона';
         	return {'0': 2, '1': 4, '2': 80}[a];
	   }
	},//methods
		
	mounted() {
		
		
	},//mounted
	
}//root

const app = Vue.createApp(root);
const vm = app.mount('#app');