class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
      
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 
 

print("?") 

print(yang is yin.yang) 
del(yang)


