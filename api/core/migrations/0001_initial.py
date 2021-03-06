# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 12:53
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.CharField(choices=[('Agent', 'Agent')], max_length=256)),
                ('output_dir', models.CharField(blank=True, max_length=256, null=True)),
                ('params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AgentMemory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.CharField(choices=[('Memory', 'Memory')], max_length=256)),
                ('params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.CharField(choices=[('NoOpBridge', 'NoOpBridge'), ('LatentBridge', 'LatentBridge')], max_length=256)),
                ('state_size', models.CharField(blank=True, max_length=64, null=True)),
                ('params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Decoder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.CharField(blank=True, choices=[('Decoder', 'Decoder')], max_length=256, null=True)),
                ('definition', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Encoder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.CharField(blank=True, choices=[('Encoder', 'Encoder')], max_length=256, null=True)),
                ('definition', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.CharField(choices=[('GymEnvironment', 'GymEnvironment')], max_length=256)),
                ('env_id', models.CharField(max_length=256)),
                ('params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Estimator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.CharField(choices=[('Estimator', 'Estimator')], max_length=256)),
                ('output_dir', models.CharField(blank=True, max_length=256, null=True)),
                ('params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256)),
                ('output_dir', models.CharField(max_length=256)),
                ('train_hooks', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('FinalOpsHook', 'FinalOpsHook'), ('GlobalStepWaiterHook', 'GlobalStepWaiterHook'), ('StopAfterNEvalsHook', 'StopAfterNEvalsHook'), ('NanTensorHook', 'NanTensorHook'), ('StepLoggingTensorHook', 'StepLoggingTensorHook'), ('StopAtStepHook', 'StopAtStepHook'), ('StepCheckpointSaverHook', 'StepCheckpointSaverHook'), ('StepCounterHook', 'StepCounterHook'), ('StepSummarySaverHook', 'StepSummarySaverHook'), ('EpisodeLoggingTensorHook', 'EpisodeLoggingTensorHook'), ('StopAtEpisodeHook', 'StopAtEpisodeHook'), ('EpisodeSummarySaverHook', 'EpisodeSummarySaverHook')], max_length=256), blank=True, default=[], null=True, size=None)),
                ('eval_hooks', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), blank=True, default=[], null=True, size=None)),
                ('eval_every_n_steps', models.IntegerField(default=1000)),
                ('train_steps', models.IntegerField(default=10000)),
                ('eval_steps', models.IntegerField(default=10)),
                ('eval_delay_secs', models.IntegerField(default=0)),
                ('continuous_eval_throttle_secs', models.IntegerField(default=60)),
                ('delay_workers_by_global_step', models.BooleanField(default=False)),
                ('export_strategies', models.CharField(blank=True, max_length=256, null=True)),
                ('train_steps_per_iteration', models.IntegerField(default=1000)),
                ('estimator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Estimator')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InputData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('input_type', models.CharField(blank=True, choices=[('NUMPY', 'NUMPY'), ('PANDAS', 'PANDAS')], max_length=256, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Loss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.CharField(choices=[('absolute_difference', 'absolute_difference'), ('log_loss', 'log_loss'), ('mean_squared_error', 'mean_squared_error'), ('softmax_cross_entropy', 'softmax_cross_entropy'), ('sigmoid_cross_entropy', 'sigmoid_cross_entropy'), ('hinge_loss', 'hinge_loss'), ('cosine_distance', 'cosine_distance'), ('kullback_leibler_divergence', 'kullback_leibler_divergence'), ('poisson_loss', 'poisson_loss'), ('huber_loss', 'huber_loss'), ('clipped_delta_loss', 'clipped_delta_loss')], max_length=256)),
                ('params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.CharField(choices=[('streaming_true_positives', 'streaming_true_positives'), ('streaming_true_negatives', 'streaming_true_negatives'), ('streaming_false_positives', 'streaming_false_positives'), ('streaming_false_negatives', 'streaming_false_negatives'), ('streaming_mean', 'streaming_mean'), ('streaming_mean_tensor', 'streaming_mean_tensor'), ('streaming_accuracy', 'streaming_accuracy'), ('streaming_precision', 'streaming_precision'), ('streaming_recall', 'streaming_recall'), ('streaming_auc', 'streaming_auc'), ('streaming_specificity_at_sensitivity', 'streaming_specificity_at_sensitivity'), ('streaming_sensitivity_at_specificity', 'streaming_sensitivity_at_specificity'), ('streaming_precision_at_thresholds', 'streaming_precision_at_thresholds'), ('streaming_recall_at_thresholds', 'streaming_recall_at_thresholds'), ('streaming_sparse_recall_at_k', 'streaming_sparse_recall_at_k'), ('streaming_sparse_precision_at_k', 'streaming_sparse_precision_at_k'), ('streaming_sparse_average_precision_at_k', 'streaming_sparse_average_precision_at_k'), ('streaming_mean_absolute_error', 'streaming_mean_absolute_error'), ('streaming_mean_relative_error', 'streaming_mean_relative_error'), ('streaming_mean_squared_error', 'streaming_mean_squared_error'), ('streaming_root_mean_squared_error', 'streaming_root_mean_squared_error'), ('streaming_covariance', 'streaming_covariance'), ('streaming_pearson_correlation', 'streaming_pearson_correlation'), ('streaming_mean_cosine_distance', 'streaming_mean_cosine_distance'), ('streaming_percentage_less', 'streaming_percentage_less'), ('streaming_mean_iou', 'streaming_mean_iou')], max_length=256)),
                ('params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Optimizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.CharField(choices=[('adadelta', 'adadelta'), ('adagrad', 'adagrad'), ('adam', 'adam'), ('ftrl', 'ftrl'), ('momentum', 'momentum'), ('nesterov', 'nesterov'), ('rmsprop', 'rmsprop'), ('sgd', 'sgd')], max_length=256)),
                ('learning_rate', models.FloatField(default=0.0001)),
                ('decay_type', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('decay_steps', models.IntegerField(default=100)),
                ('decay_rate', models.FloatField(default=0.99)),
                ('start_decay_at', models.IntegerField(default=0)),
                ('stop_decay_at', models.IntegerField(default=2147483647)),
                ('min_learning_rate', models.FloatField(default=1e-12)),
                ('staircase', models.BooleanField(default=False)),
                ('sync_replicas', models.IntegerField(default=0)),
                ('sync_replicas_to_aggregate', models.IntegerField(default=0)),
                ('params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.CharField(blank=True, choices=[('ParallelTextPipeline', 'ParallelTextPipeline'), ('TFRecordSourceSequencePipeline', 'TFRecordSourceSequencePipeline'), ('TFRecordImagePipeline', 'TFRecordImagePipeline'), ('ImageCaptioningPipeline', 'ImageCaptioningPipeline')], max_length=256, null=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('definition', models.TextField()),
                ('dynamic_pad', models.BooleanField(default=True)),
                ('bucket_boundaries', models.BooleanField(default=False)),
                ('batch_size', models.IntegerField(default=64)),
                ('num_epochs', models.IntegerField(default=1)),
                ('min_after_dequeue', models.IntegerField(default=5000)),
                ('num_threads', models.IntegerField(default=3)),
                ('shuffle', models.BooleanField(default=False)),
                ('allow_smaller_final_batch', models.BooleanField(default=True)),
                ('params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PolyaxonModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.CharField(choices=[('Classifier', 'Classifier'), ('Regressor', 'Regressor'), ('Generator', 'Generator'), ('DQNModel', 'DQNModel'), ('DDQNModel', 'DDQNModel'), ('NAFModel', 'NAFModel')], max_length=256)),
                ('summaries', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('activations', 'activations'), ('loss', 'loss'), ('gradients', 'gradients'), ('variables', 'variables'), ('learning_rate', 'learning_rate'), ('image_input', 'image_input'), ('image_result', 'image_result'), ('exploration', 'exploration'), ('reward', 'reward')], max_length=256), default=['all'], size=None)),
                ('clip_gradients', models.FloatField(default=5.0)),
                ('clip_embed_gradients', models.FloatField(default=0.1)),
                ('params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
                ('bridge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Bridge')),
                ('decoder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Decoder')),
                ('encoder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Encoder')),
                ('eval_metrics', models.ManyToManyField(to='core.Metric')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RLExperiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256)),
                ('output_dir', models.CharField(max_length=256)),
                ('train_hooks', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('FinalOpsHook', 'FinalOpsHook'), ('GlobalStepWaiterHook', 'GlobalStepWaiterHook'), ('StopAfterNEvalsHook', 'StopAfterNEvalsHook'), ('NanTensorHook', 'NanTensorHook'), ('StepLoggingTensorHook', 'StepLoggingTensorHook'), ('StopAtStepHook', 'StopAtStepHook'), ('StepCheckpointSaverHook', 'StepCheckpointSaverHook'), ('StepCounterHook', 'StepCounterHook'), ('StepSummarySaverHook', 'StepSummarySaverHook'), ('EpisodeLoggingTensorHook', 'EpisodeLoggingTensorHook'), ('StopAtEpisodeHook', 'StopAtEpisodeHook'), ('EpisodeSummarySaverHook', 'EpisodeSummarySaverHook')], max_length=256), blank=True, default=[], null=True, size=None)),
                ('eval_hooks', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), blank=True, default=[], null=True, size=None)),
                ('eval_every_n_steps', models.IntegerField(default=1000)),
                ('train_steps', models.IntegerField(default=10000)),
                ('eval_steps', models.IntegerField(default=10)),
                ('eval_delay_secs', models.IntegerField(default=0)),
                ('continuous_eval_throttle_secs', models.IntegerField(default=60)),
                ('delay_workers_by_global_step', models.BooleanField(default=False)),
                ('export_strategies', models.CharField(blank=True, max_length=256, null=True)),
                ('train_steps_per_iteration', models.IntegerField(default=1000)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Agent')),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Environment')),
                ('eval_metrics', models.ManyToManyField(blank=True, to='core.Metric')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PolyaxonModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RunConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('model_dir', models.CharField(blank=True, max_length=256, null=True)),
                ('master', models.CharField(blank=True, max_length=256, null=True)),
                ('num_cores', models.IntegerField(default=0)),
                ('log_device_placement', models.BooleanField(default=False)),
                ('gpu_memory_fraction', models.FloatField(default=1.0)),
                ('tf_random_seed', models.IntegerField(blank=True, null=True)),
                ('save_summary_steps', models.IntegerField(blank=True, default=100, null=True)),
                ('save_checkpoints_secs', models.IntegerField(blank=True, default=600, null=True)),
                ('save_checkpoints_steps', models.IntegerField(blank=True, null=True)),
                ('keep_checkpoint_max', models.IntegerField(blank=True, default=5, null=True)),
                ('keep_checkpoint_every_n_hours', models.IntegerField(blank=True, default=10000, null=True)),
                ('evaluation_master', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('gpu_allow_growth', models.BooleanField(default=False)),
                ('cluster_config', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubGraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('definition', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='rlexperiment',
            name='run_config',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.RunConfig'),
        ),
        migrations.AddField(
            model_name='polyaxonmodel',
            name='graph',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SubGraph'),
        ),
        migrations.AddField(
            model_name='polyaxonmodel',
            name='loss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Loss'),
        ),
        migrations.AddField(
            model_name='polyaxonmodel',
            name='optimizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Optimizer'),
        ),
        migrations.AddField(
            model_name='inputdata',
            name='pipeline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pipeline'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='eval_input_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eval', to='core.InputData'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='eval_metrics',
            field=models.ManyToManyField(blank=True, to='core.Metric'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PolyaxonModel'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='run_config',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.RunConfig'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='train_input_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='train', to='core.InputData'),
        ),
        migrations.AddField(
            model_name='agent',
            name='memory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.AgentMemory'),
        ),
    ]
