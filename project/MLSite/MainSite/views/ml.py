from flask import render_template, request
import pandas as pd
from MainSite.views.tree import tree_learn
from MainSite.views.i_cluster import i_cluster
from MainSite.views.r_forest import r_forest



supervised = ['tree']
unsupervised = ['i_cluster']
def ml_page():
    if request.method == 'POST':
        file = request.form.get('myFile')
        target = request.form.get('exampleRadios')
        method = request.form.get('method')

        if target == "-1":
            if method == "i_cluster":
                n_clusters = request.form.get('n_clusters')
                if int(n_clusters) <= 0:
                    return render_template('ml.html')
                affinity = request.form.get('affinity')
                features, ran, ran1, file = i_cluster(file, int(n_clusters), affinity)
                print(ran)
                return render_template('result_cluster.html', features=features, ran=ran, ran1=ran1, file=file)


        elif target:
            if method == "tree":
                max_depth = request.form.get('max_depth')
                if int(max_depth) <= 0:
                    return render_template('ml.html')
                min_samples_split = request.form.get('min_samples_split')
                if int(min_samples_split) <= 1:
                    return render_template('ml.html')
                min_samples_leaf = request.form.get('min_samples_leaf')
                if int(min_samples_leaf ) <= 1:
                    return render_template('ml.html')
                max_features = request.form.get('max_features')
                mae, mdae, rmse, ran, file = tree_learn(file, target, int(max_depth), int(min_samples_split), int(min_samples_leaf), int(max_features))
                return render_template('results.html', mae=mae, mdae=mdae, rmse=rmse, ran=ran, file=file)

            if method == "r_forest":
                n_estimators = request.form.get('n_estimators')
                #if int(n_estimators) <= 0:
                    #return render_template('ml.html')
                max_depth = request.form.get('max_depth')
                #if int(max_depth) <= 0:
                    #return render_template('ml.html')
                min_samples_split = request.form.get('min_samples_split')
                #if int(min_samples_split) <= 1:
                    #return render_template('ml.html')
                min_samples_leaf = request.form.get('min_samples_leaf')
                #if int(min_samples_leaf ) <= 1:
                    #return render_template('ml.html')
                mae, mdae, rmse, ran, file = r_forest(file, target, int(n_estimators), int(max_depth), int(min_samples_leaf), int(min_samples_split))
                return render_template('results_forest.html', mae=mae, mdae=mdae, rmse=rmse, ran=ran, file=file)





        elif file and method == "tree":
            df = pd.read_excel(file, 0)
            return render_template('ml_columns.html', file=file, columns=list(df.columns), method=method)

        elif file and method == "r_forest":
            df = pd.read_excel(file, 0)
            return render_template('ml_columns_forest.html', file=file, columns=list(df.columns), method=method)

        elif file and method == "i_cluster":
            return render_template('ml_columns_cluster.html', file=file, method=method)
        else:
            print('nooooo')
    return render_template('ml.html')
