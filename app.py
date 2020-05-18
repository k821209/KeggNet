

import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout, to_agraph
import pygraphviz as pgv
import matplotlib.pyplot as plt
import numpy as np
from flask import request, jsonify, Flask
from flask_cors import CORS
import base64
import random
import string
import json
# from adjustText import adjust_text

def get_net(inText,outFile,figsize=(15,10),minDegree=4,subGraph=False,method='neato'):
    fr = inText
    fr = [x.strip() for x in fr.split('\n') if x != '']
    import pandas as pd
    df = pd.DataFrame() 
    for each in fr:
        if each[0:3] == 'ko:':
            #print(1,each)
            koID   = each.split()[0]
            try:
                koSym  = each.split()[1].replace(';','')
                koDesc = ' '.join(each.split()[1:]).replace(koSym,'').replace(';','')
                df.at[koID,'Sym'] = koSym
                df.at[koID,'Desc'] = koDesc
            except IndexError:
                df.at[koID,'Sym'] = None
                df.at[koID,'Desc'] = None
        else:
            #print(2,each)
            if each.strip() == '': continue
            koID   = each.split()[0]
            koDesc  = ' '.join(each.split()[1:-1])
            df.at[koID,'Sym'] = None
            df.at[koID,'Desc'] = koDesc

    dfNet = pd.DataFrame()
    i = 0 
    for each in fr:
        if each[0:3] == 'ko:':
            koID       = each.split()[0]
        else:
            if each.strip() == '':continue
            briteClass = each.split()[0]
            koID = ''
        if koID != '':
            dfNet.at[i, 'Source'] = briteClass
            dfNet.at[i, 'Target'] = koID
            i += 1

    plt.figure(figsize=figsize)
    basalSize = 40
    nodes = list(set(dfNet.values.ravel()))
    

    edges = dfNet.values
    
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    Gorig = G.copy()
    if subGraph:
        G = G.subgraph([x for x,y in dict(G.degree()).items() if y > minDegree])
    c = [0 if 'ko:' in x else G.degree[x] for x in G.nodes ]
    c = [x if x < 20 else 20 for x in c]
    s = [1 if 'ko:' in x else basalSize+Gorig.degree[x]*100 for x in G.nodes]
    sD3 = [2 if 'ko:' in x else Gorig.degree[x] for x in G.nodes]
    sMax = max(sD3)
    sDic = dict(zip(G.nodes,sD3))
    l = {}
    for x in G.nodes:
        if 'ko:' in x:
            # l[x] = df.loc[x]['Sym']
            l[x] = ''
        else:
            if Gorig.degree(x) > minDegree:
                l[x] = '{desc} ({degree})'.format(desc=' '.join(df.loc[x]['Desc'].split()),degree=Gorig.degree[x])
            else: l[x] = ''
    
    pos = graphviz_layout(G,method)#  ‘dot’, ‘twopi’, ‘fdp’, ‘sfdp’, ‘circo’
    text = nx.draw_networkx_labels(G,pos,labels=l,font_size=13)
    nodes = nx.draw_networkx_nodes(G,pos,node_color=c,node_size=s,cmap='Reds')
    nodes.set_edgecolor('gray')
    nx.draw_networkx_edges(G,pos,alpha=0.1)
    # for _,t in text.items():
    #    t.set_rotation(45)
    plt.axis('off')
    plt.margins(x=0.3)
    #plt.tight_layout()
    plt.savefig('./static/'+outFile+'.png',bbox_inches='tight',dpi=200)
    
    # network json creation 
    g = G 
    nodes = [{'name': '', 'id': str(i), 'size':sDic[i],'group':1} if i[0:3] == 'ko:' else {'name': l[i], 'id': str(i),'size':2+20*(sDic[i]/sMax),'group':2} for i in g.nodes()]
    links = [{'source': u[0], 'target': u[1]}
         for u in g.edges()]
    with open('./static/'+outFile+'.json', 'w') as f:
        json.dump({'nodes': nodes, 'links': links},
              f, indent=4,)
    
    


app = Flask(__name__)
CORS(app)

@app.route('/KeggNetApi',methods=['POST'])
def showNet():
    message = request.get_json(force=True)        
    inText  = message['text'].strip()
    #print(inText)        
    randomstring = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])          
    get_net(inText,randomstring)
    response = {}
    response['outFile'] = randomstring+'.png'
    response['outJson'] = randomstring+'.json'
    return jsonify(response)                    # html�� �뺤뀛�덈━瑜� �쒖씠�� �щ㎎�쇰줈 留뚮뱾�� 蹂대깂  
