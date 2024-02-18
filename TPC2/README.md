# TPC2:
## 2024-02-18
## Autor:
A95458

Inês Meneses de Castro

## Resumo

```python
re.sub(pattern, repl, string, count=0, flags=0)
```

Headers
Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"

In: \#Exemplo

Out: \<h1>Exemplo\</h1>


Bold: pedaços de texto entre "\*\*":

In: Este é um \*\*exemplo\*\* ...

Out: Este é um \<b>exemplo\</b> ...


Itálico: pedaços de texto entre "\*":

In: Este é um \*exemplo\* ...

Out: Este é um \<i>exemplo\</i> ...


Lista numerada:

In:

  1. Primeiro item
  2. Segundo item
  3. Terceiro item
     
Out:

  \<ol>
  
    <li>Primeiro item</li>
    
    <li>Segundo item</li>
    
    <li>Terceiro item</li>
    
  \</ol>
  

  
Link: [texto](endereço URL)

In: Como pode ser consultado em \[página da UC](http://www.uc.pt)

Out: Como pode ser consultado em \<a href="http://www.uc.pt">página da UC\</a>


Imagem: ![texto alternativo](path para a imagem)

In: Como se vê na imagem seguinte: \![imagem dum coelho](http://www.coellho.com) ...

Out: Como se vê na imagem seguinte: \<img src="http://www.coellho.com" alt="imagem dum coelho"/> ...
    
