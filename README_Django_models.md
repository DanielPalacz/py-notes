
### Django - MODELS - repetition questions
```
Basics:
  1. What is meaning of options 'null' and 'blank' in model fields? What is difference between them?
  2. How to set default value for the Django model field?
  3. What are four typical types of fields on Django models?
  4. How to change default table name correlated with Django model?
  5. There is 'SlugField' type - explain what is use case for it? How to implement automatic slugifying in Django?
  6. What are other three-four types of fields on Django models?
  7. How to use 'choices' field Django model parameter?
  8. How to create User object without calling default password hashing mechanism? Will it happen when create_user method is used?
  9. How to get from db all objects that meets specific condition, for example title="Django"?
 10. How to limit query result in ORM to only first 10 be displayed?
 11. How to implement data validation in Django models?


Relationship between Models:
 101. What is use case of 'related_name' in ForeignKey model field?
 102. How to create model in Many-to-Many relationship?
 103. What happens if we set 'on_delete=models.CASCADE' in ForeignKey model field and correlated parent object will be deleted?
 104. How to get correlated objects in One-To-Many relationship?
 105. Is index automatically created in db during creating One-To-Many relationsips?
 106. What are three use cases when indexes are automatically created by Django?
 107. In Many-To-Many relationship what default name of Mediatory-Table?
 108. How to optimize ORM fetching query in relationships? What is difference between 'select_related' and 'prefetch_related'?

Other operations on Models:
 201. How to use method 'save?' Can it be overiden?
 202. How to create additional indexes when you want to filter data by using specific fields?
 203. What is difference between validation in model field (for example validators) and method 'clean()' in model?

Advanced model's functionalities:
 301. How to define Custom Object Manager for the model? For what can it be helpful? What about custom QuerySets?
 302. Advanced Querying with Django ORM: annotate(), aggregate(), Q, F, Subqueries
```
