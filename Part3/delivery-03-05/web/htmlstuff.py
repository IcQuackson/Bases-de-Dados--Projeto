# this is a python file



create_delete_supplier_form = """
<form action="" method="GET" style="border-style: solid; boder-color: black;">
        <div>Manage Suppliers</div>
        <div> <input id="ainsert" name="operation" type="radio" value="CREATESUPPLIER" required> <label
                        for="insert">Insert<label>
                                <input id="aremove" name="operation" type="radio" value="DELETESUPPLIER"> <label
                                        for="aremove">Remove<label>
        </div>
                                <input type="text" id="msname" value="{ms_name}" placeholder="insert name" maxlength="80" name='ms_name' required/>
                                <input type="tel" length='9' maxlength="9" id="msnif" value="{ms_nif}" placeholder="insert nif"  name='ms_nif' required/>
	 <input type="submit" value="Submit">
</form>
"""


modify_product_suppliers_form = """
<form action="" method="GET" style="border-style: solid; boder-color: black;" >
        <div>Remove supplier from product</div>
        <input id="ainsert" name="operation" type="hidden" value="deleteSuppliers" > 
                                <input type="text" maxlength="80"  value="{mp_name}" placeholder="insert ean"  name="mp_ean" required/>
                                <input type="tel" maxlength="9" length="9"  value="{mp_nif}" placeholder="insert nif"  name="mp_nif" required/>
	 <input type="submit" value="Remove supplier">
</form>





"""




manage_categories_form = """
<!--PARTE A-->
<form action="" method="GET" style="border-style: solid; boder-color: black;" >
        <div>Manage Categories</div>
        <div> <input id="ainsert" name="operation" type="radio" value="insert" required> <label
                        for="insert">Insert<label>
                                <input id="aremove" name="operation" type="radio" value="delete"> <label
                                        for="aremove">Remove<label>
        </div>
        <div> <input id="acategory" name="type" type="radio" value="Super Category" required> <label
                        for="acategory">Super Category<label> <input id="asubcategory" name="type" type="radio"
                                        value="Simple Category">
                                <label for="asubcategory">Simple Category<label> </div> <input type="text" id="category"
                placeholder="insert category name" maxlength="80" name='category' required> <input type="submit" value="Submit">
</form>
"""

create_product_form = """
<!--PARTE B-->
<form action="" method="GET" style="border-style: solid; boder-color: black;">
    <h1>Create Product</h1> 
    <div style="boder-style: 4px black solid;"> 


<input name='executequery' type="hidden" value="1" \>
<label>EAN <input type="text" maxlength="20" name="ean" value="{ean}" placeholder="insert the product identifier (ean)" required\> </label>

<label> Description
 <input type="text" name="description" value="{description}" placeholder="insert the description for a product" required\> 
</label>
<input type="hidden" name='operation' value='createProduct'/>

<label> Category
 <input type="text"  maxlength="80" name="category" value="{category}" placeholder="category" required\> 
</label>

<label>Primary supplier
 <input type="tel" length="9"  name="supplierprim" value="{supplierprim}" placeholder="primary supplier" required\> 
</label>

    </div>

<input type="submit" value="Submit">
<div>
</div>
</form>
<form style="border-style: solid; boder-color: black;" >
<h1>Add Suppliers to Product</h1>

<input name='executequery' type="hidden" value="1" \>
<div>
<input type="hidden" name='operation' value='updateSuppliers'/>
<label>EAN <input type="text" minlength='1' maxlength="20" name="ean" value="{ean}" placeholder="insert the product identifier (ean)" required\> </label>

 <input type="tel" maxlength="9" minlength="9" length="9" name="supplierprim" value="{supplierprim}" placeholder="primary supplier" required\> 

<div>

<div>
 <input type="tel" length="9" class="supsec" maxlength="9" minlength="9" name="suppliersec1" value="{suppliersec1}" placeholder="secondary supplier" required\> 
</div>

<div>
 <input class='supsec' type="tel" length="9" maxlength="9" minlength="9" name="suppliersec2" value="{suppliersec2}" placeholder="secondary supplier" required\> 
</div>

<div>
 <input class='supsec' type="tel" maxlength="9" length="9" minlength="9" name="suppliersec3" value="{suppliersec3}"  placeholder="secondary supplier" required\> 
</div>


</div>


</div>

<input type="submit" value="Add suppliers to product">
</form>
"""

webpagehead = """Content-type:text/html\n\n
<html>      
<head>         
<title>Supermarket Big Data</title>
</head>        
<body>        
"""

row_css = """ margin-right: 10px; margin-left: 10px; padding: 10px; border-style: dashed solid; display: flex; flex-direction:row ;border-color: blue; border-width: 1px;font-size: 15px; display: flexbox; flex-flow: row; justify-content: space-between; """

supplier_row = """
<div>
                        <div style="display:inline-block">
                                <div style="display:inline-block; width:300px;"><span style="font-weight: bold">Name:</span> {name}</div>
                                <div style="display:inline-block; width:300px;"><span style="font-weight: bold">Nif:</span> {nif}</div>
                        </div>
<div>
<div style="margin-right:auto; margin-left:0px;">
								<a  href="?operation=DELETESUPPLIER&ms_nif={nif}"  {style} >Remove</a>
</div>

</div>

</div>
"""


product_row = """
<div style="margin-right: 10px; margin-left: 10px; padding: 10px; border-style: dashed solid; display: flex; flex-direction:row ;border-color: blue; border-width: 1px;font-size: 15px; display: flexbox; flex-flow: row; justify-content: space-between;">
        <div >
        <div style="width:200px; display:inline-block"><span style="font-weight: bold">Ean:</span> {ean}</div>
        <div style="display:inline-block"><span style="font-weight: bold">Description:</span> {description}</div>
        <div><span style="font-weight: 505">Category: </span><a href="list_sub_aux.cgi?name={category}" style="display:inline-block">{category}</a></div>
        </div>
		<div   style="width:400px; display:flex; justify-content: space-between;">
		<a href="designation.cgi?ean={ean}" style="font-size: 15px; padding-right:30px;">Change description</a>
        <a  href="ShowReplenishments.cgi?ean={ean}" style'font-size: 15px; padding-left:300px;' >Show replenishments</a>
        <a id='remover' style='margin-left:auto;color:red' href="?operation=DELETE&ean={ean}">Delete</a> 
</div>
</div>
"""



category_row = """
                <div
                        style="margin-right: 10px; margin-left: 10px; padding: 10px; border-style: dashed solid; display: flex; flex-direction:row ;border-color: blue; border-width: 1px;font-size: 15px; display: flexbox; flex-flow: row; justify-content: space-between;">
                        <div style="display:inline-block">
                                <div style="display:inline-block; width:300px;"><span style="font-weight: bold">Name:</span> {name}</div>
                                <div style="display:inline-block; width:300px;"><span style="font-weight: bold">Type:</span> {type}</div>
								<a style="display:inline-block; width:300px;" href="list_sub_aux.cgi?category={name}">View composition</a>
                        </div>
                        <a id='remover' href="?category={name}&type={type}&operation=DELETE" style=" margin-left: auto; margin-right: 0px; text-decoration: underline; color:red ;display: inline-block; ">Remove</a>
</div>
"""







remove_style = """ style=" margin-left: auto; margin-right: 0px; text-decoration: underline; color:red ;display: inline-block;" """

error = """
                <div style='border-radius:10px; border-style: green solid;  padding-top:1px; padding-left:3px; background-color:green;'>
                        <h1 style='color:white;'>An error has occured <h1>
                                        <p style='padding-left:15px; padding-bottom:15px; font-size:15px;'>{}</p>
                                        <p style='padding-left:15px; padding-bottom:15px; font-size:15px;'>No changes were made.</p>
                </div>
"""

success = """
                <div style='border-radius:10px; border-style: green solid;  padding-top:1px; padding-left:3px; background-color:green;'>
                        <h2 style='color:white;'>{}<h2>

<p>A word from our sponsor confirming further your success:</p>
<h6 style='padding-top: 0px; margin-top:-25px; font-weight: normal; '>We do not take any responsability for thirdparty's behavior.</h6>
                                        <p style='padding-left:15px; padding-bottom:15px; font-size:15px; font-weight: normal;'>{}</p>
                </div>
"""






category_row_add_to_form = """
                <div
                        style="margin-right: 10px; margin-left: 10px; padding: 10px; border-style: dashed solid; display: flex; flex-direction:row ;border-color: blue; border-width: 1px;font-size: 15px; display: flexbox; flex-flow: row; justify-content: space-between;">
                        <div style="display:inline-block">
                                <div style="display:inline-block; width:300px;"><span style="font-weight: bold">Name:</span> {}</div>
                                <div style="display:inline-block; width:300px;"><span style="font-weight: bold">Type:</span> {}</div>
                        </div>
                        <a id='remover' href="" onclick='addToForm(event, {},{})'
                                style=" margin-left: auto; margin-right: 0px; text-decoration: underline; color:red ;display: inline-block; ">Remove</a>
                </div>
"""


error = """
                <div style='border-radius:10px; border-style: red solid;  padding-top:1px; padding-left:3px; background-color:red;'>
                        <h1 style='color:white;'>An error has occured <h1>
                                        <p style='padding-left:15px; padding-bottom:15px; font-size:15px;'>{}</p>
                </div>
"""

tabs_js = """
<script>
function openPage(pageName,elmnt,color) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }
  document.getElementById(pageName).style.display = "block";
  elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it
//document.getElementsByClassName("tabcontent")[0].click();
</script>
"""
tabs_css = """

<style>
* Set height of body and the document to 100% to enable "full page tabs" */
body, html {
  height: 100%;
  margin: 0;
  font-family: Arial;
  background-color: blue;
}

/* Style tab links */
.tablink {
  background-color: #555;
  color: white;
  float: left;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 14px 16px;
  font-size: 17px;
  width: 25%;
}

.tablink:hover {
  background-color: #777;
}

/* Style the tab content (and add height:100% for full page content) */
.tabcontent {
}

#Primary_Suppliers {background-color: red;}
#Super_Categories {background-color: green;}
#Contact {background-color: blue;}
#About {background-color: orange;}

</style>
"""



apihead = """Content-type:text/json\n\n"""
#apihead = """Content-Type: application\json"""
