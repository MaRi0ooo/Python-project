s = 'In a distant, but not so unrealistic, future \
    where mankind has abandoned earth because it has \
    become covered with trash from products sold by \
    the powerful multi-national Buy N Large corporation, \
    WALLE, a garbage collecting robot has been left to \
    clean up the mess. Mesmerized with trinkets of Earth’s \
    history and show tunes, WALLE is alone on Earth except \
    for a sprightly pet cockroach. One day, EVE, a sleek \
    (and dangerous) reconnaissance robot, is sent to Earth to \
    find proof that life is once again sustainable.'

# Довжина рядка s наведеного тексту
print(len(s))
# Текст в нижньому регістрі
print(s.lower())
# Замініть всі входження слова WALLE на WALL-E
print(s.replace('WALLE', 'WALL-E'))
# Підрахуйте, скільки разів в тексті було використано слово Earth
print(s.count("Earth"))