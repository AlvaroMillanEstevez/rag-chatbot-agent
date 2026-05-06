# Manual demo de la aplicación

Esta aplicación permite gestionar usuarios, productos, pedidos y documentación interna.

## Usuarios

El panel de usuarios permite consultar, crear, editar y archivar usuarios.

## Archivado de usuarios

Para archivar un usuario, el administrador debe entrar en el panel de usuarios, seleccionar el usuario correspondiente y pulsar la opción de archivar.

Los usuarios archivados no se eliminan de la base de datos. Solo dejan de aparecer en los listados principales.

El archivado se utiliza para conservar el historial y evitar la pérdida de información sensible.

## Productos

El panel de productos permite gestionar el catálogo de productos, incluyendo nombre, descripción, precio, stock y estado.

## Pedidos

El panel de pedidos permite revisar pedidos realizados, consultar su estado y actualizar información relacionada con el proceso de entrega.

## Seguridad

La información sensible no debe mostrarse a usuarios sin permisos.

Solo los usuarios autenticados pueden acceder al panel de administración.

Las acciones críticas deben estar protegidas mediante permisos o roles.

## Chatbot

El chatbot debe responder solo usando la documentación disponible.

Si la información no aparece en los documentos, el chatbot debe indicar que no tiene información suficiente.

El chatbot debe mostrar las fuentes utilizadas para generar cada respuesta.