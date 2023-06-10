import pyperclip
# los inputs mas o menos pueden ir por lenguaje natural, ya que para entender las instrucciones utiliza palabras clave y las demas las ignora

class machado():
    contexto_historico_europa = str("Durante los siglos XIX y XX, por toda Europa hubo una gran inestabilidad tanto política como social.\n"+
                                    "Durante este siglo hubo una gran cantidad de cambios políticos, culturales, sociales... que entre otras cosas se vieron reflejados en la literatura. Por ejemplo, por el lado soviético estuvo la Revolución Rusa, que desencadenó la creación de la URSS, que terminó siendo una potencia a nivel mundial en diversos ámbitos y adoptaba ideologías comunistas, marxistas, leninistas...\n"+
                                    "También por toda Europa hubo otros sucesos que provocaron grandes cambios como las crisis económicas, las clases bajas sufrieron mucho y lucharon por sus derechos, la movilización de las poblaciones desde las áreas agrícolas a las ciudades con fin de trabajar en las empresas... Y todo esto llevo a la crisis de fin de siglo.\n"+
                                    "Durante finales del siglo XIX y por todo el siglo XX el mundo se dividió en dos grandes potencias económicas, sociales, ideológicas y armamentísticas, por un lado la URSS y por el otro, Estados Unidos junto a la OTAN.\n"+
                                    "También Alemania tuvo una gran importancia, sobre todo en el lado bélico, ya que provocó las dos grandes guerras de la historia de la humanidad, que fueron seguidas por la tensión que supuso a la humanidad la posibilidad del enfrentamiento entre las dos grandes potencias que imperaron en el mundo durante todo ese siglo (la guerra fría), con sucesos como la crisis de los misiles de Cuba...\n"+
                                    "Todo esto contribuyó en el avance técnico y tecnológico (con la creación del telégrafo, la producción en masa de automóviles, la radio y la televisión, los tranvías, el cine...) resultado de la industrialización liderada por una burguesía rica y dominante, pese a los movimientos obreros y sociales que lograron la mejora de las condiciones laborales y de vida de las clases medias y bajas.")
    contexto_historico_españa = str("En España a los sucesos vividos en el resto de Europa se le suman otros propios de España, como la desaparición de las últimas colonias, la pérdida del Sahara, Cuba, Filipinas..., un intento de republica que terminó con una guerra civil seguida de una dictadura, la vuelta a la democracia y muchas cosas más.\n"+
                                    "Durante el siglo XIX se intentó modernizar el país y crear estructuras sociales y políticas, pero no se consiguió y España se quedó atrasada en comparación con el resto de países occidentales, el sistema político no funcionaba, la industrialización no se produjo con la velocidad que lo hizo en el resto de Europa, había mucho analfabetismo, el caciquismo estaba muy expandido, es decir, burgueses que compraban los botos para tener el poder y a la vez estos mismo eran terratenientes de los campos que labraban las clases medias y bajas, y a la vez había una burguesía que se lucraba de las clases medias y bajas para tener vidas muy acomodadas y permitiéndose muchos lujos. Todo esto se vio reflejado en la literatura de la época con el Regeneracionismo.\n"
                                    "En la mayoría del país había centros educativos con sistemas pedagógicos anticuados, que se basaban en la memorización, pero la gran mayoría de escritores estuvieron en la Institución Libre de Enseñanza, donde se utilizaron nuevos métodos de pedagógicos y gracias a esta se introdujeron métodos pedagógicos y científicos desarrollados en el resto de Europa y ayudaron junto al modernismo a mejorar la enseñanza en el país.\n"+
                                    "A principios del siglo XX se vivió la semana trágica, que aumentó el malestar en la sociedad por enviar más tropas a marruecos. Después hubo una república, en la que se intentó arreglar un poco la situación en la que se encontraba el país, mejorando la educación, creando leyes, intentando mejorar la situación de los trabajadores... Pero esto se terminó tras el golpe de estado planeado por los generales Mola, Sanjurjo y Franco, y tras la sospechosa muerte de los primeros dos, hubo una guerra civil liderada por Franco que duro desde el 1936 hasta el 1939 y termino con imposición de una dictadura que lideraba este general. Dado a la crisis producida por la guerra civil y la dictadura España no entro en la Gran Guerra (la primera guerra mundial) y al no querer enfrentarse a Estados Unidos, solamente ayudó a Hitler enviando tropas para ayudarlo a combatir al comunismo (la brigada azul). Tras la derrota del fascismo en la segunda guerra mundial España intentó mejorar las relaciones con los otros países, e intento meterse en la unión europea y en la OTAN, pero al ser una dictadura fascista no les dejaron, por lo que España tuvo que tomar medidas para mejorar su situación política, social, económica y las relaciones con los otros países miembros de estas organizaciones. Para mejorar la situación económica se devaluó la peseta, se intentó fomentar la inversión extranjera... Y tras la muerte de Franco, comenzó una transición hacia una democracia más occidentalizada.")
    contexto_literario = str("A finales del siglo XIX y principios del siglo XX había dos corrientes literarias, la estética y la ética. La primera tiene relación con el modernismo, mientras que la segunda se relaciona con la generación del 98. En la corriente estética se buscaba la belleza, mientras que en la ética se presentaban las personas que intentaron sacar el país adelante.\n"+
                             "Fruto de la crisis que se estaba viviendo en Europa, en los países hispanohablantes surgieron autores que optaron por una nueva literatura en contra del realismo y el naturalismo. Debido a la literatura que trataban y a la época a la que pertenecieron, a estos autores se los puede clasificar en dos distintos grupos simultáneamente, el Modernismo y la generación del 98. El primer término en un origen se utilizaba como insulto por los autores en contra de las novedades y la innovación literaria hasta que a finales del siglo XIX un grupo de escritores decidieron sentirse orgullosos de nombrarse así. Y varios años después de la invención del término “modernismo” Azorín creo el término “generación del 98”, el cual recoge los autores del final de ese siglo, sensibilizados ante el desastre y que daban importancia al avance del pensamiento literario de otros países. Algunos autores de este segundo grupo son Unamuno, Valle Inclán, Azorín, Benavente...")
    
    semejanzas_98_moderno = str("La generación del 98 y el Modernismo, pese a que se sitúan en una época parecida, eran movimientos literarios distintos, pero presentaban varias características en común:\n"+
                                "Debido a la situación de la época, la crisis, la desigualdad entre clases... en ambos se aprecian rasgos de rebeldía y de deseo de cambios.\n"+
                                "También los dos surgieron del malestar causado por la crisis que se estaba viviendo en Europa y al que se sumaba en España, por la desigualdad, la perdida de las últimas colonias...\n"+
                                "También los dos cambian la literatura de la época modernizándola.")
    diferenzias_98_moderno = str("La principal diferencia que presentan los dos grupos es el estilo literario que utilizaban. A finales del siglo XIX había dos estilos literarios predominantes, la visión estética que se centraba en la belleza, y la visión ética, que se centraba en las personas que intentaban mejorar la situación de la época. El Modernismo adoptaba la primera, mientras que la generación del 98 adoptaba la segunda.\n"+
                                 "También el origen es distinto, ya que el Modernismo tiene un origen un poco más antiguo, ya que en el siglo XIX se utilizaba como insulto a los autores innovadores, hasta que un grupo de escritores lo adopto sintiéndose orgullosos de ello. Mientras que “la generación del 98” la creo Azorín a principios del siglo XX para nombrar a algunos autores del final del siglo pasado incluyéndose a el mismo.\n"+
                                 "Por otra parte, el modernismo se movía más por temas aristocráticos y de la burguesía, mientras que la generación del 98 trataba más sobre el pueblo español. Por este mismo motivo, el lenguaje que utilizaban también era distinto, los modernistas utilizaban muchos neologismos y cultismos, mientras que los de la generación del 98 hacían uso de un lenguaje que todo el mundo fuese capaz de entender.")    
    
    temas = str("Los temas que tocaba eran:\n"+
                "·La muerte: un tema muy recurrente en las obras de Machado era la muerte, debido a la muerte de su mujer. Para introducir este tema en sus obras utiliza el simbolismo, haciendo uso de símbolos como las estaciones del año, los ríos, los atardeceres, las sombras...\n"+
                "·Otro tema importante es el amor, el cual se puede diferenciar en dos, el que sentía por su difunta mujer y el que luego sentía por otra mujer(Guiomar). En muchas obras se mezcla con la muerte por el primer tipo de amor, pero en algunas se centra más en el segundo.\n"+
                "·También se aprecia la preocupación por España que sentía, lo cual es uno de los rasgos de modernismo y de la generación del 98, debido a la crisis que se estaba viviendo en Europa y en España. Se preocupaba por el presente y por el futuro de España, y tocaba tanto lo que opinaba que estaba mal, como el cariño que le tenía al país."+
                "·Otro tema que solia tocar eran los campos de castilla, que se caracterizan por estar vacios y ser esplanadas enormes sin nada a la vista, pero le gustaban ya que una de sus aficiones era caminar.")
    
    obras = {"soledades":str("Esta fue su primera obra, cuando era más joven y rebelde, lo cual se aprecia en la obra e intento ocultar más tarde cuando tuvo más edad. Es una obra modernista e intimista y donde abunda el simbolismo (como el agua estancada para hacer referencia a la muerte...). Algunos autores de la actualidad como Rosalía recuerdan bastante al estilo que tenía.  Los temas principales que se tocan en la obra son la muerte, dios, y el paso del tiempo.\n"),
             "campos de castilla":str("Esta obra la escribió cuando fue a Castilla donde conoció a su primera mujer y a donde volvió cuando ella enfermo y posteriormente murió por tuberculosis, más concretamente en Soria. Ha machado le gustaban mucho las esplanadas deshabitadas de las que esta región abunda, ya que una de sus aficiones era caminar.\n"+
                                      "Los temas que toca son el amor por la naturaleza y por castilla, la preocupación por España... La obra tiene poemas intimistas, abundan las descripciones, y se aparte a el del centro de atención para ponerlo en la sociedad. También se aprecia su preocupación por el presente y el futuro del país.\n"),
             "nuevas canciones":str("Esta obra está compuesta por una gran variedad de poemas breves de distintos estilos y temas, intimistas, apreciando sus tierras... Pero son de menor calidad a los que escribió en Campos de Castilla y durante esta temporada dejo de escribir tanto como lo que solía hacer.\n"),
             "ultimos poemas":str("Después de las nuevas canciones, escribió bastante poco, su obra más importante de ese tiempo fue “Canciones a Guiomar”.  Pero con la guerra civil española, tuvo que escapar por los pirineos, escribió un libro “La Guerra” y murió pocos meses después.\n")}
    
class Yo_voy_soñando_caminos():
    all = str('Este es un poema de Antonio Machado titulado "Yo voy soñando caminos", publicado en su obra "Soledades, galerías y otros poemas". El poema puede estar basado en las obras de la poeta Rosalía de Castro, y evoca los sentimientos de amor y añoranza del poeta mientras camina por un entorno lleno de simbolismo. El paisaje se oscurece a medida que el amor desaparece.\n'+
              'El poema está compuesto por 24 versos octosílabos y está dividido en dos partes, en la primera admira la belleza del paisaje lleno de simbolismo y la segunda poco a poco va oscureciéndose a la vez que va desapareciendo el amor.')

class El_mañana_efímero():
    all = 'Este es un poema llamado "El mañana efímero" de Antonio Machado, que se encuentra en "Campos de Castilla". El poema expresa la idea de que la vida es corta y efímera. Machado tenía dos visiones de España: una tradicionalista y anclada en el pasado, y otra más joven y optimista que buscaba un futuro mejor a través del trabajo. El poema está estructurado en dos partes, la primera crítica a la sociedad española y la segunda expresando su deseo de que evolucione hacia una sociedad más moderna. Está escrito con versos heptasílabos y endecasílabos con rima consonante.'

class Noche_de_verano():
    all = 'Este es un poema de Antonio Machado llamado "Noche de Verano", perteneciente a "Campos de Castilla", describe un viejo pueblo en una noche de verano. El poeta se enfoca en la soledad y el vacío que siente, proyectándolos en la descripción del entorno. El poema tiene 12 versos que son endecasílabos y heptasílabos y se estructuran en dos partes: la descripción del paisaje y la presentación del yo (osea, el) en soledad. El poema está lleno de simbolismos para representar sus sentimientos.'

class Soñé_que_tú_me_llevabas():
    all = ("Este es el poema “soñé que tú me llevabas”, que forma parte de la obra “Campos de Castilla”. Está escrito en un estilo narrativo, descriptivo y con mucho simbolismo. El tema principal del poema es la muerte, la soledad y la tristeza que sentía tras la muerte de su primera mujer, relatando un sueño lleno de simbolismo en el que era conducido por su difunta esposa.\n"+
           "Está formado por 16 versos octosílabos.")

class A_orillas_del_Duero():
    all = 'Este es un resumen del poema "A orillas del Duero" de Antonio Machado, también incluido en "Campos de Castilla". El poema describe el paisaje de Castilla y compara su belleza del pasado con su decadencia actuales (osea, de esa época). Machado critica la falta de actitud crítica de las personas y su falta de cultura y analfabetismo. El poema utiliza metáforas y símiles para describir el paisaje. El poema cierra con una visión pesimista de un país estancado en el pasado.'

while True:
    prompt = input().lower().split()
    
    if "europa" in prompt:
        pyperclip.copy(machado.contexto_historico_europa)
    elif "españa" in prompt and "literario" not in prompt:
        pyperclip.copy(machado.contexto_historico_españa)
    elif "literario" in prompt:
        pyperclip.copy(machado.contexto_literario)
    elif "direrencias" in prompt:
        pyperclip.copy(machado.diferenzias_98_moderno)
    elif "semejanzas" in prompt or "similitudes" in prompt or "parecido" in prompt or "parecidos" in prompt:
        pyperclip.copy(machado.semejanzas_98_moderno)
    elif "temas" in prompt:
        pyperclip.copy(machado.temas)
    elif "castilla" in prompt:
        pyperclip.copy(machado.obras["campos de castilla"])
    elif "soledades" in prompt:
        pyperclip.copy(machado.obras["soledades"])
    elif "nuevas" in prompt:
        pyperclip.copy(machado.obras["nuevas canciones"])
    elif "ultimos" in prompt or "guerra" in prompt:
        pyperclip.copy(machado.obras["ultimos poemas"])
    elif "obras" in prompt:
        pyperclip.copy(str("Soledades, galerías y otros poemas:\n" + machado.obras["soledades"]+
                           "\nCampos de Castilla:\n" + machado.obras["campos de castilla"]+
                           "\nNuevas canciones:\n" + machado.obras["nuevas canciones"]+
                           "\nÚltimos poemas:\n" + machado.obras["ultimos poemas"]))
    elif "soñe" in prompt or "soñé" in prompt or "llevabas" in prompt:
        pyperclip.copy(Soñé_que_tú_me_llevabas.all)
    elif "efimero" in prompt or "efímero" in prompt:
        pyperclip.copy(El_mañana_efímero.all)
    elif "verano" in prompt or "noche" in prompt:
        pyperclip.copy(Noche_de_verano.all)
    elif "duero" in prompt or "orillas" in prompt or "orilla" in prompt:
        pyperclip.copy(A_orillas_del_Duero.all)
    elif "caminos" in prompt:
        pyperclip.copy(Yo_voy_soñando_caminos.all)