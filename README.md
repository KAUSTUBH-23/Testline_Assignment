Simply run the program and install the modules used if not already present.

Output:
Current Quiz Data Structure: dict_keys(['quiz'])
Current DataFrame Columns: Index(['id', 'description', 'difficulty_level', 'topic', 'is_published',
       'created_at', 'updated_at', 'detailed_solution', 'type', 'is_mandatory',
       'show_in_feed', 'pyq_label', 'topic_id', 'reading_material_id',
       'fixed_at', 'fix_summary', 'created_by', 'updated_by', 'quiz_level',
       'question_from', 'language', 'photo_url', 'photo_solution_url',
       'is_saved', 'tag', 'options', 'is_correct'],
      dtype='object')
     id                                        description difficulty_level  \
0  1827  The tissue which has free surface that faces e...             None   
1  1828  Epithelial tissue is distinguished from connec...             None   
2  1829  The ciliated columnar epithelial cells in huma...             None   
3  1830                The squamous epithelium is found in             None   
4  1831  The kind of epithelium which forms the inner w...             None   

                                 topic  is_published  \
0  structural organisation in animals           True   
1  structural organisation in animals           True   
2  structural organisation in animals           True   
3  structural organisation in animals           True   
4  structural organisation in animals           True   

                      created_at                     updated_at  \
0  2024-07-02T12:43:34.360+05:30  2024-11-30T18:39:20.587+05:30   
1  2024-07-02T12:50:56.100+05:30  2024-11-30T18:39:20.788+05:30   
2  2024-07-02T12:54:25.824+05:30  2024-11-30T18:39:20.990+05:30   
3  2024-07-02T12:56:48.204+05:30  2024-11-30T18:39:21.192+05:30   
4  2024-07-02T12:58:51.241+05:30  2024-11-30T18:39:21.398+05:30   

                                   detailed_solution type  is_mandatory  ...  \
0  **Explanation:**\n\nThe tissue that has a free...              False  ...   
1  **Epithelial Tissue**\n\n* Epithelial tissue i...              False  ...   
2  **Explanation:**\n\nCiliated columnar epitheli...              False  ...   
3  **Explanation:**\n\nSquamous epithelium is a t...              False  ...   
4  **Answer is correct because:**\n\nSquamous epi...              False  ...   

   updated_by quiz_level  question_from  language photo_url  \
0        None       None         Q-bank      None      None   
1        None       None         Q-bank      None      None   
2        None       None         Q-bank      None      None   
3        None       None         Q-bank      None      None   
4        None       None         Q-bank      None      None   

  photo_solution_url is_saved tag  \
0               None    False       
1               None    False       
2               None    False       
3               None    False       
4               None    False       

                                             options is_correct  
0  [{'id': 7321, 'description': 'Muscular tissue'...       True  
1  [{'id': 7325, 'description': 'large extracellu...       True  
2  [{'id': 7329, 'description': 'Eustachian tube ...       True  
3  [{'id': 7333, 'description': 'stomach', 'quest...       True  
4  [{'id': 7337, 'description': 'cuboidal epithel...       True  

[5 rows x 27 columns]
Index(['question_id', 'description', 'difficulty_level', 'topic',
       'is_published', 'created_at', 'updated_at', 'detailed_solution', 'type',
       'is_mandatory', 'show_in_feed', 'pyq_label', 'topic_id',
       'reading_material_id', 'fixed_at', 'fix_summary', 'created_by',
       'updated_by', 'quiz_level', 'question_from', 'language', 'photo_url',
       'photo_solution_url', 'is_saved', 'tag', 'options', 'is_correct'],
      dtype='object')

Historical DataFrame Columns: Index(['quiz_id', 'question_id', 'selected_option', 'is_correct', 'topic'], dtype='object')
Processed Historical DataFrame:
   quiz_id question_id  selected_option  is_correct  \
0       51        2523            10109        True   
1       51        2529            10130        True   
2       51        2533            10149       False   
3       51        2534            10151        True   
4       51        2535            10155       False   

                         topic  
0  Body Fluids and Circulation  
1  Body Fluids and Circulation  
2  Body Fluids and Circulation  
3  Body Fluids and Circulation  
4  Body Fluids and Circulation  

Weak Areas:
Empty DataFrame
Columns: [topic, accuracy]
Index: []

Recommendations:
1. You're improving! Keep up the consistent practice.

Student Persona: Strong in structural organisation in animals  (100%) but needs work in structural organisation in animals  (100%)
Predicted NEET Rank: 2999 (Based on mock data)


![testline_output](https://github.com/user-attachments/assets/ca9e75c9-bf4b-4fcd-857d-5b799e36f766)

