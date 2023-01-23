import streamlit as st
import re
st.set_page_config("Site Progress",":pencil:","wide","collapsed")





a = st.sidebar.radio('Select What Service You Need :', ["Welcome Page" ,"page_1" , "caluculator"])
if a=="Welcome Page":

    st.title("Welcome To Our Site Please Select The Service You Need From The SideBar")
    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")

elif a=="page_1":

    st.title('ARAR transmission line :red[( 380 KV DC ) ]')

    x=st.button("Smile")
    if x== True :
     # st.balloons()
        st.snow()

    st.markdown('Streamlit is **_really_ cool**.')
    st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")

    col_1,col_2,col_3,col_4,col_5=st.columns(5)

    with col_1.form(key='my_form'):
        username = st.text_input('Username')
        password = st.text_input('Password')
        st.form_submit_button('Login')

    if username=="m" and password=="m":
        st.balloons()

        col_2.header(f"welcome Back Mr. {username}")

    col_1=st.columns(1)

    st.text_input("Enter your Equation down here ")
    st.number_input("enter")
    st.button('Click me')
    st.checkbox('I agree')
    st.radio('Pick one', ['cats', 'dogs'])
    st.selectbox('Pick one', ['cats', 'dogs'])
    st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
    st.slider('Pick a number', 0, 100)
    st.select_slider('Pick a size', ['S', 'M', 'L'])
    st.text_input('First name')
    st.number_input('Pick a number', 0, 10)
    st.text_area('Text to translate')
    st.date_input('Your birthday')
    st.time_input('Meeting time')
    st.file_uploader('Upload a CSV')
    st.camera_input("Take a picture")
    st.color_picker('Pick a color')
    st.header("transmission line 380 KV DC",)

    st.subheader("Please Press This button to know more....")


    "hello world"
    st.text('This is some text.')
    st.metric("ManPower",50,100)
    col_1,col_2,col_3,col_4 =st.columns(4)

    col_1.title(":blue[section:1]")
    col_2.title(":blue[section:2]")
    col_3.title(":blue[section:3]")
    col_4.title(":blue[section:4]")
    col_1.color_picker('Pick A Color', '#00f800')
elif a=="caluculator":
    eq=str(st.text_input("Enter Your Equation And Gett it Solved :) "))   
    x=re.findall(r"\d+/\d+",eq)
    for i in x :
        s=i.split("/")
        s=float(s[0])/float(s[1])
        eq=eq.replace(i,str(s))
    st.text(f" Result = {eq}")    
    x=re.findall(r"\d+\*\d+",eq)
    for i in x :
        s=i.split("*")
        s=float(s[0])*float(s[1])
        eq=eq.replace(i,str(s))
    st.text(f" Result = {eq}") 
    x=re.findall(r"\d*.?\d*\-\d*.?\d*",eq)
    
         
