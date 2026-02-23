((python-mode
  . ((eglot-workspace-configuration
      . (:pylsp (:configurationSources ["pycodestyle"] ; string array: ["flake8"] or ["pycodestyle"] (default)
                                       :plugins (;; Note autopep uses some pycodestyle settings further down to avoid redefining things namely aggressive, exclude, hangClosing, ignore, maxLineLength and select
                                                 :autopep8
                                                 (:enabled :json-false) ; boolean: true (default) or false
						 :black
						 (:enabled t)
                                                 :flake8
                                                 (:config nil ; string: null (default)
                                                          :enabled :json-false ; boolean: true or false (default)
                                                          :exclude [] ; string array: [] (default)
                                                          :executable "flake8" ; string: "flake8" (default)
                                                          :extendIgnore [] ; string array: [] (default)
                                                          :filename nil ; string: null (default)
                                                          :hangClosing nil ; boolean: true or false; null (default)
                                                          :ignore [] ; string array: [] (default)
                                                          :indentSize nil ; integer: null (default)
                                                          :maxComplexity nil ; integer: null (default)
                                                          :maxLineLength nil ; integer: null (default)
                                                          :perFileIgnores [] ; string array: [] (default) e.g. ["file_path.py:W305,W304"]
                                                          :select nil) ; string array: null (default)
                                                 :jedi
                                                 (:auto_import_modules ["numpy"] ; string array: ["numpy"] (default)
                                                                       :env_vars nil ; object: null (default)
                                                                       :environment nil ; string: null (default)
                                                                       :extra_paths []) ; string array: [] (default)
                                                 :jedi_completion
                                                 (:cache_for ["pandas" "numpy" "tensorflow" "matplotlib"] ; string array: ["pandas", "numpy", "tensorflow", "matplotlib"] (default)
                                                             :eager :json-false ; boolean: true or false (default)
                                                             :enabled t ; boolean: true (default) or false
                                                             :fuzzy :json-false ; boolean: true or false (default)
                                                             :include_class_objects :json-false ; boolean: true or false (default)
                                                             :include_function_objects :json-false ; boolean: true or false (default)
                                                             :include_params t ; boolean: true (default) or false
                                                             :resolve_at_most 25) ; integer: 25 (default)
                                                 :jedi_definition
                                                 (:enabled t ; boolean: true (default) or false
                                                           :follow_builtin_definitions t ; boolean: true (default) or false
                                                           :follow_builtin_imports t ; boolean: true (default) or false
                                                           :follow_imports t) ; boolean: true (default) or false
                                                 :jedi_hover
                                                 (:enabled t) ; boolean: true (default) or false
                                                 :jedi_references
                                                 (:enabled t) ; boolean: true (default) or false
                                                 :jedi_signature_help
                                                 (:enabled t) ; boolean: true (default) or false
                                                 :jedi_symbols
                                                 (:all_scopes t ; boolean: true (default) or false
                                                              :enabled t ; boolean: true (default) or false
                                                              :include_import_symbols t) ; boolean: true (default) or false
                                                 :mccabe
                                                 (:enabled :json-false ; boolean: true (default) or false
                                                           :threshold 15) ; integer: 15 (default)
                                                 :preload
                                                 (:enabled :json-false ; boolean: true (default) or false
                                                           :modules []) ; string array: [] (default)
                                                 :pycodestyle
                                                 (:enabled :json-false ; boolean: true (default) or false
                                                           :exclude [] ; string array: [] (default)
                                                           :filename [] ; string array: [] (default)
                                                           :hangClosing nil ; boolean: true or false; null (default)
                                                           :ignore [] ; string array: [] (default)
                                                           :indentSize nil ; integer: null (default)
                                                           :maxLineLength nil ; integer: null (default)
                                                           :select nil) ; string array: null (default)
                                                 :pydocstyle
                                                 (:addIgnore [] ; string array: [] (default)
                                                             :addSelect [] ; string array: [] (default)
                                                             :convention nil ; string: "google", "numpy" or "pep257"; null (default)
                                                             :enabled :json-false ; boolean: true or false (default)
                                                             :ignore [] ; string array: [] (default)
                                                             :match "(?!test_).*\\.py" ; string: "(?!test_).*\\.py" (default)
                                                             :matchDir "[^\\.].*" ; string: "[^\\.].*" (default)
                                                             :select nil) ; string array: null (default)
                                                 :pyflakes
                                                 (:enabled :json-false) ; boolean: true (default) or false
                                                 :pylint
                                                 (:args [] ; string array: [] (default)
                                                        :enabled t ; boolean: true or false (default)
                                                        :executable "pylint") ; string: null (default)
                                                 :rope_autoimport
                                                 (:code_actions (:enabled t) ; boolean: true (default) or false
                                                                :completions (:enabled t) ; boolean: true (default) or false
                                                                :enabled :json-false ; boolean: true or false (default)
                                                                :memory :json-false) ; boolean: true or false (default)
                                                 :rope_completion
                                                 (:eager :json-false ; boolean: true or false (default)
                                                         :enabled t) ; boolean: true or false (default)
                                                 :yapf
                                                 (:enabled :json-false)) ; boolean: true (default) or false
                                       :rope
                                       (:extensionModules nil ; string: null (default)
                                                          :ropeFolder nil)))))))
