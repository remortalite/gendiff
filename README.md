### Hexlet tests and linter status:
[![Actions Status](https://github.com/remortalite/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/remortalite/python-project-50/actions)
[![Python CI](https://github.com/remortalite/python-project-50/actions/workflows/build.yaml/badge.svg)](https://github.com/remortalite/python-project-50/actions/workflows/build.yaml)
[![Maintainability](https://api.codeclimate.com/v1/badges/9322302759fa8fdd9823/maintainability)](https://codeclimate.com/github/remortalite/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9322302759fa8fdd9823/test_coverage)](https://codeclimate.com/github/remortalite/python-project-50/test_coverage)


# Генератор отличий

Программа позволяет пользователю получить различия двух json или yaml файлов, и вывести их на печать или в json формат.

# Установка и запуск

```bash
make install

make gendiff
```

Или можно установить программу в виртуальное окружение:

```bash
make install package-install publish

gendiff -h
```

# Аргументы командной строки

`gendiff filepath1 filepath2 [-f json|plain|stylish]`

Где: 
* `filename{1,2}` -- пути до файлов

* `-f`, `--format [json/plain/stylish]` -- формат вывода различий

# Example:

[![asciicast](https://asciinema.org/a/nUm0QAamnNyrRkQCMJHwqLVVO.svg)](https://asciinema.org/a/nUm0QAamnNyrRkQCMJHwqLVVO)
