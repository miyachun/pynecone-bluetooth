import pynecone as pc
import typing as t
import bluetooth

bd_addr = "XXX"

class Message(pc.Base):
    message: str

class State(pc.State):    
    prompt = ""
    messages: t.List[Message] = []    
    def sendData(self):
        port = 1
        sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        sock.connect((bd_addr, port))
        prompt=self.prompt
        self.messages.append(prompt)
        self.messages.append(' ')
        sock.send(prompt)
        sock.close()

def index():
    return pc.center(
        pc.vstack(
            pc.heading("HC06藍牙傳輸", font_size="1.5em"),
            pc.input(placeholder="輸入內容", on_blur=State.set_prompt),
            pc.button(
                "送出",
                on_click=State.sendData,
                width="100%",
            ),           
            pc.text(State.messages, color_scheme="green"),
            width="60vw",            
            bg="white",
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),      
        width="100%",
        height="100vh",
        bg="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%)",
    )


app = pc.App(state=State)
app.add_page(index, title="Pynecone Bluetooth")
app.compile()
        
        
        
        
       
       
       
       
      
    


