# Перепишите алгоритм починки (со слайда про вложенные инструкции) без вложенных инструкций if.
# Сравните полученный код с тем, что приведен на слайде. В каком коде проще разобраться, на ваш взгляд?

"""
is_moving = input('Is it moving? ')  # Он движется?
if is_moving == 'yes':  # да
   should_move = input('Should it move? ')  # Должен ли он двигаться?
   if should_move == 'yes':  # да
       print("Don't touch")  # Не прикасайся
   else:
       print('Use glue')  # Используйте клей
else:
   should_move = input('Should it move? ')  # Должен ли он двигаться?
   if should_move == 'yes':  # да
       print('Use oil')  # Используйте масло
   else:
       print("Don't touch")  # Не прикасайся
"""

is_moving = input('Is it moving? ')
should_move = input('Should it move? ')
if is_moving == 'yes' and should_move == 'no':
    print('Use glue')
elif is_moving == 'no' and should_move == 'yes':
    print('Use oil')
else:
    print("Don't touch")
