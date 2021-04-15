import streamlit as st
import pickle

model = pickle.load(open('RFR_abalone_model.pkl','rb'))

def main():
    st.title("Abalone age predictor app ")
    st.markdown("##### Are you trying to predict the age of abalone?\n##### So let's try predicting the age.")
    st.write('---')
    
    Sex=st.selectbox('Sex of abalone?',('M','F','I'))
    if(Sex=='M'):
        Sex=3
    elif(Sex=='F'):
        Sex=1  
    else:
        Sex=2
    
    Length = st.number_input('Length of abalone?', 0.0, 0.81, 0.01)
    
    Diameter = st.number_input('Diameter of abalone?',0.0,0.65,0.01)
    
    Height = st.number_input('Height of abalone?',0.0,1.13,0.01)
    
    Whole_weight = st.number_input('Whole Weight of abalone?',0.0,2.83,0.01)
    
    Shucked_weight = st.number_input('Shucked Weight of abalone?',0.0,1.49,0.01)
                              
    Viscera_weight = st.number_input('Viscera Weight of abalone?',0.0,0.76,0.01)
                              
    Shell_weight = st.number_input('Shell Weight of abalone?',0.0,1.0,0.01)
    
    
    
    st.write('---')
    if st.button('Age',key='predict'):
        try: 
            Model=model
            prediction=Model.predict([[Sex,Length,Diameter,Height,Whole_weight,Shucked_weight,Viscera_weight,Shell_weight]])
            output = round(prediction[0],4)
            if output<0:
                st.warning("Age coming in negative.Invalid Input Given")
            else:
                st.success("The age of abalone is---> {}".format(output))
        except:
            st.warning("Something went wrong\nTry again")
            
            
            
            
            
if __name__ == "__main__":
    main()            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    
    
