
submitFunction = """
<script>
async function submit(event){
	event.preventDefault()
		

}
</script>
"""

# pergunta a
preserveURL = """
<script>
window.history.pushState("", "", 'http://web.tecnico.ulisboa.pt/alexandre.e.bento/{}.cgi');
</script>
"""

submit_sec_supplier1 = """() => {{const this_sup_nif = {}; let sc = getElementsByTagName("supsec"); console.log(sc); alert(sc); }}
"""


submit_sec_supplier = r"""() => {{console.log(\'ded\')}} """

scrollToSuppliers =  """
<script> 
window.addEventListener('load', (event) => {
 	getElementById('supplierstable').scrollIntoView(1); 
});

</script>
"""

removeCategory = """
<script>
window.history.pushState("", "", 'http://web.tecnico.ulisboa.pt/alexandre.e.bento/pergunta_a.cgi');
 async function removeCategory(event, category_name, type){
//event.preventDefault()
/*
const operation = "DELETE";
const data = {
operation, category_name, type
}



var res = await fetch(`?category=${category}&type=${type}&operation=${operation}`)
res = await res.text().then(text => console.log(text))
alert(res)
*/
}


</script>
""" 
