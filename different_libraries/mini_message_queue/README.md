

### Running commands:
```
\mini_message_queue$ PYTHONPATH=. python app.py
\mini_message_queue$ PYTHONPATH=. pytest tests/test_queue.py
```


### Version1
```
Broker
    │
    ▼
Queue

To jest całkowicie poprawne na początek, bo nie masz jeszcze obiektów Producer i Consumer.

Tak naprawdę Twój app.py jest jednocześnie producentem i konsumentem. To on robi:
broker.publish(msg)
 - czyli zachowuje się jak Producer.

A potem:
broker.consume()
 - czyli zachowuje się jak Consumer.



Dlaczego Broker istnieje?
Na tym etapie jest cienką warstwą (ang. thin wrapper). I to jest całkowicie normalne.
Po co więc on jest? Bo z czasem zacznie robić coraz więcej.
To, że obecnie Twój Broker jest tylko delegatem: nie oznacza, że jest źle zaprojektowany.
    Wręcz przeciwnie. To częsty sposób rozwijania architektury.
    Tworzysz miejsce, w którym w przyszłości będzie skupiona logika zarządzania wiadomościami, ale nie wymyślasz tej logiki na zapas.
    Dzięki temu projekt rośnie razem z wymaganiami, zamiast zaczynać od rozbudowanej architektury, która jeszcze nie jest potrzebna.



Ostatecznie architektura może wyglądać tak
Producer
     │
     ▼
 Broker
 ┌──────────────┐
 │ routing      │
 │ retry        │
 │ ack          │
 │ metrics      │
 │ logging      │
 └──────────────┘
     │
     ▼
 Queue
     │
     ▼
Consumer
```


### Broker:
```
Broker nie jest zdefiniowany przez model Producer–Consumer, tylko jest komponentem, który może być używany w takim modelu.

Broker to komponent pośredniczący między producentami (Producer) a konsumentami (Consumer), odpowiedzialny zaprzyjmowanie, przechowywanie, kierowanie i dostarczanie wiadomości.

Broker zarządza przepływem wiadomości pomiędzy producentami i konsumentami.


Jedna ważna uwaga. 
Warto rozróżnić odpowiedzialność od interfejsu.Na przykład:

retry() nie musi być metodą publiczną. Może być wewnętrznym mechanizmem uruchamianym przez timer lub scheduler.
metrics() również nie musi być metodą typu broker.metrics(). Broker może po prostu aktualizować liczniki podczas publish() i consume().
routing() często nie jest osobną metodą, tylko fragmentem implementacji publish().
```

